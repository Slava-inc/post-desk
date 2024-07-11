from django.forms import ModelForm
from article.models import Article, Message

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = ['text']

class DetailForm(ModelForm):
	class Meta:
		model = Article
		fields = ['tittle', 'text', 'category']