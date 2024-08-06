from django.shortcuts import render, redirect
from article.models import Article, Message
from .forms import ArticleForm, MessageForm, DetailForm
from django.conf import settings
from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
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

	if request.method == 'POST':
		form = ArticleForm(request.POST, instance=article)

		if form.is_valid():
			form.save()
			
			return redirect(settings.SITE_URL)
	else:
		form = ArticleForm(instance=article)
		
	return render(request, 'article/detail.html', {'article': article, 'form': form})

# def create(request):

# 	if request.method == 'POST':
# 		form = ArticleForm(request.POST)

# 		if form.is_valid():
# 			form.save()
			
# 			return redirect(settings.SITE_URL)
# 	else:
# 		form = ArticleForm()
		
# 	return render(request, 'article/create.html', {'form': form})

class ArticleCreate(CreateView):
	# Указываем нашу разработанную форму
	form_class = ArticleForm
	# модель товаров
	model = Article
    # и новый шаблон, в котором используется форма.
	template_name = 'article/create.html'
    
	def get_success_url(self):
		next_url = self.request.GET.get('next')
		if next_url:
			return next_url 
		return '/article/index/'
	
	def form_valid(self, form):
		article = form.save(commit=False)
		article.user = self.request.user 
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['next_url'] = self.request.GET.get('next')
        # send_news_notification(object=self.object, action='post_add')
		return context  

		
def detail(request, pk):
	article = Article.objects.get(pk=pk)

	form = DetailForm(request.GET, instance=article)
	if request.method == 'POST':
		form = DetailForm(request.POST, instance=article)
		return render(request, 'article/detail.html', {'article': article, 'form': form, 'user_from': request.user})		
	return render(request, 'article/detail.html', {'article': article, 'form': form, 'user_from': request.user})	
