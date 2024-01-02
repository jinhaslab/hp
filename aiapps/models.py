from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.models import MarkdownxField  # Import MarkdownxField

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aiapps_posts')
    body = MarkdownxField()  # Updated to use MarkdownxField
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slide_link = models.URLField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='post_images/', default='ocean1.jpg')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
