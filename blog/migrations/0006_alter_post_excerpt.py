# Generated by Django 5.0 on 2023-12-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_excerpt_alter_post_slide_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(default='', max_length=200),
        ),
    ]
