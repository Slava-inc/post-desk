from django.urls import path, include
from article.views import detail, update
from article.views import ArticlesList,ArticleCreate, message_create
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

app_name = 'article'

urlpatterns = [
	path('article/index/', ArticlesList.as_view(), name='/article_list'),
    path('', include('protect.urls')),
	path('ckeditor/', include('ckeditor_uploader.urls')),
    path('article/index/<int:pk>', detail, name='detail'),
    path('article/create/', ArticleCreate.as_view(), name='create'),
    path('article/update/<int:pk>', update, name='update'),
    # path('sign/', include('sign.urls')),
    # path('article/message/<int:pk>', MessageCreate.as_view(), name='message_create'),
    path('article/message/<int:pk>', login_required(message_create), name='message_create')
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)