# from django.db import models
# from django.contrib.auth.models import User

# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField


# class Article(models.Model):
#     tittle = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     content_upload = RichTextUploadingField(blank=True, null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     likes = models.ManyToManyField('Article', through='UserArticle') 
    

# class UserArticle(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)


# class Message(models.Model):
#     text = models.CharField(max_length=255)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     user_from = models.ForeignKey(User, on_delete=models.CASCADE)

