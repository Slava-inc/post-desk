from django.shortcuts import render
from desk.models import Article
from .forms import ArticleForm

def index(request):
	articles = Article.objects.all()
	return render(request, 'article/index.html', {'articles': articles})
	
def detail(request):
	article = Article.objects.get(pk=1)
	
	if request.method == 'POST':
		form = ArticleForm(request.POST, instance=article)
		
		if form.isvalid():
			form.save()
			
			return render('detail')
	else:
		form = ArticleForm(instance=article)
		
	return render(request, 'article/detail.html', {'article': article, 'form': form})
