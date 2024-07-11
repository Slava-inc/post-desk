from django.shortcuts import render

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from article.models import Category, Message

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['is_not_author'] = not self.request.user.groups.filter(name = 'authors').exists()
        models = Category.objects.all()
        context['models'] = models
        return context


class MessageCreate(CreateView):
	model = Message
	template_name = 'article/message.html'
	fields = ['text',]


	# def message_create(request, pk):
		
	# 	article = Article.objects.get(pk)
	# 	form = MessageForm(request.POST)
	# 	return render(request, 'article/message.html', {'article': article, 'form': form})	