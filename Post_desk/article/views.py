from django.shortcuts import render, redirect
from article.models import Article, Message
from .forms import ArticleForm, MessageForm, DetailForm
from django.conf import settings
from django.views.generic import ListView
from django.http import HttpResponseRedirect
import os


def message_create(request, pk):
	article = Article.objects.get(id=pk)
	mes = Message.objects.filter(article=article, user_from=request.user).first()
	
	if mes == None:
		mes = Message(article = article, user_from=request.user)
		mes.save()

	if request.method == 'POST':
		form = MessageForm(request.POST, instance=mes)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/article/index')
		else:
			form = MessageForm(instance=mes)

	return render(request, 'article/message.html', {'article': article, 'user': request.user, 'form': form, 'message': mes})

def index(request):
	articles = Article.objects.all()
	return render(request, 'article/view.html', {'articles': articles})

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
	# mes = Message(article = article, user_from=request.user)
	# mes.save()

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
		form = DetailForm(request.POST, instance=article)
		return render(request, 'article/detail.html', {'article': article, 'form': form, 'user_from': request.user})		
	return render(request, 'article/detail.html', {'article': article, 'form': form, 'user_from': request.user})	
