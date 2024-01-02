from django.views import generic
from django.db.models import Q
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from django.http import HttpResponseForbidden
from django.shortcuts import render
import markdown 
from django.utils.safestring import mark_safe

from .forms import PostForm


class PostList(generic.ListView):
    model = Post
    template_name = 'note/index.html'
    context_object_name = 'object_list'
    paginate_by = 5  # Adjust the number of posts you want per page

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        author_name = self.request.GET.get('author_name')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(body__icontains=query) | Q(excerpt__icontains=query)
            )
    
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)

        page = self.request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['object_list'] = posts
        return context


#class CreatePostView(LoginRequiredMixin, CreateView):
class CreatePostView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  # Use the custom form
    success_url = reverse_lazy('note:home')
    permission_required = ('note.add_post',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'note/post_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Get the post object from the context
        post = context['object']
        # Convert the markdown content to HTML and mark it as safe (to prevent HTML escaping)
        post.body = mark_safe(markdown.markdown(post.body))
        # Update the context with the modified post
        context['object'] = post
        return context

    
class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'note/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Post.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
            return object_list
        return Post.objects.none()
    
class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm  # Use the same custom form
    template_name = 'note/edit_post.html'
    success_url = reverse_lazy('note:home')
    permission_required = 'note.change_post'

    def form_valid(self, form):
        return super().form_valid(form)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'note/delete_post.html'
    # Define where to redirect after the post is successfully deleted
    success_url = reverse_lazy('note:home')
    permission_required = 'note.delete_post'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
def custom_permission_denied_view(request, exception):
    context = {'message': "You have no authority to add a post, sorry. Please ask the administrator or jinha@dspubs.org to get authority."}
    return render(request, 'note/403.html', context, status=403)