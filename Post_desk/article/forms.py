from typing import Any
from django import forms
from django.forms import ModelForm
from article.models import Article, Message
from django.views.generic import FormView

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

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
		fields = '__all__'

class DetailForm(ModelForm):
	class Meta:
		model = Article
		fields = ['tittle', 'text', 'category']