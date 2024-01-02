# Generated by Django 5.0 on 2024-01-01 08:10

import django.db.models.deletion
import markdownx.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('excerpt', models.CharField(default='', max_length=200)),
                ('body', markdownx.models.MarkdownxField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('slide_link', models.URLField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(default='ocean1.jpg', upload_to='post_images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presentation_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]