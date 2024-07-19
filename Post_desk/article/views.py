from django.shortcuts import render, redirect
from article.models import Article, Message
from .forms import ArticleForm, MessageForm, DetailForm
from django.conf import settings
from django.views.generic import ListView
import os


# def index(request):
# 	articles = Article.objects.all()
# 	return render(request, 'article/index.html', {'articles': articles})

class ArticlesList(ListView):
	model = Article
	template_name = 'article/view.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		articles = Article.objects.all()
		context['articles'] = articles

		return context
	
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
