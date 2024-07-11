from django.shortcuts import render, redirect
from article.models import Article, Message
from .forms import ArticleForm, MessageForm, DetailForm
from django.conf import settings
from django.views.generic import CreateView
import os

def index(request):
	articles = Article.objects.all()
	return render(request, 'article/index.html', {'articles': articles})
	
def update(request, pk):
	article = Article.objects.get(pk=pk)
	if request.method == 'POST':
		form = ArticleForm(request.POST, instance=article)

		if form.is_valid():
			form.save()
			
			return redirect(settings.SITE_URL)
	else:
		form = ArticleForm(instance=article)
		
	return render(request, 'article/detail.html', {'article': article, 'form': form})


def detail(request, pk):
	article = Article.objects.get(pk=pk)
	form = DetailForm(request.GET, instance=article)
	if request.method == 'POST':
		form = MessageForm(request.POST, instance=article)
		return render(request, 'article/message.html', {'article': article, 'form': form})		
	return render(request, 'article/view.html', {'article': article, 'form': form, 'pk': pk})	
