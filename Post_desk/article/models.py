from django.db import models

from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    tittle = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, through='UserArticle', related_name='user_like') 
    category = models.ManyToManyField(Category, through='CategoryArticle')


class CategoryArticle(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class UserArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Message(models.Model):
    text = models.CharField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
