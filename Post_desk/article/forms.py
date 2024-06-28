from django.forms import ModelForm
from desk.models import Article

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'