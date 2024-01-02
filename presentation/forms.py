from django import forms
from .models import Post
from markdownx.fields import MarkdownxFormField

class PostForm(forms.ModelForm):
    body = MarkdownxFormField()

    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'body', 'image', 'slide_link']
