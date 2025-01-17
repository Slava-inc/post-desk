from typing import Any
from django import forms
from django.forms import ModelForm
from article.models import Article, Message
from django.views.generic import FormView


class ArticleForm(ModelForm):
	tittle = forms.CharField(label='tittle')
	text = forms.CharField(label='article', widget=forms.Textarea(attrs={'class': 'form-control'}))

	# def get_form_kwargs(self):
	# 	kwargs = super().get_form_kwargs()
	# 	kwargs.update({
	# 		'user': self.request.user	
	# 	})
	# 	return kwargs
		
	class Meta:
		model = Article
		# fields = '__all__'
		fields = ['tittle', 'text', 'content', 'content_upload', 'category']

class MessageForm(ModelForm):
	text = forms.CharField(label='message', widget=forms.Textarea(attrs={'class': 'form-control'}))
	# def get_form_kwargs(self):
	# 	kwargs = super().get_form_kwargs()
	# 	kwargs.update({
	# 		'article': self.request.article,
	# 		'user_from': self.request.user	
	# 	})
	# 	return kwargs

	class Meta:
		model = Message
		fields = ['text']

class DetailForm(ModelForm):
	class Meta:
		model = Article
		fields = ['tittle', 'text', 'category']