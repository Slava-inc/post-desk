from django.shortcuts import render, redirect
from article.models import Article
from .forms import ArticleForm
from django.conf import settings

def index(request):
	articles = Article.objects.all()
	return render(request, 'article/index.html', {'articles': articles})
	
def detail(request, pk):
	article = Article.objects.get(pk=pk)
	
	if request.method == 'POST':
		form = ArticleForm(request.POST, instance=article)
		
		if form.is_valid():
			form.save()
			
			return redirect(settings.SITE_URL)
	else:
		form = ArticleForm(instance=article)
		
	return render(request, 'article/detail.html', {'article': article, 'form': form})
