from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostUpdateView, PostDeleteView


app_name = 'note'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('note/new/', views.CreatePostView.as_view(), name='create_post'),
    path('note/edit/<int:pk>/', PostUpdateView.as_view(), name='edit_post'),
    path('note/delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

