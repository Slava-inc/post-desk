"""
URL configuration for Post_desk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from article.views import detail, update, create
from django.conf import settings
from django.conf.urls.static import static

from protect.views import MessageCreate
from article.views import ArticlesList, message_create
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('admin/', admin.site.urls),
	# path('article/index/', index, name='index'),
	path('article/index/', ArticlesList.as_view(), name='article_list'),
    path('', include('protect.urls')),
	path('ckeditor/', include('ckeditor_uploader.urls')),
    path('article/index/<int:pk>', detail, name='detail'),
    path('article/create/', create, name='create'),
    path('article/update/<int:pk>', update, name='update'),
    path('sign/', include('sign.urls')),
    # path('article/message/<int:pk>', MessageCreate.as_view(), name='message_create'),
    path('article/message/<int:pk>', login_required(message_create), name='message_create')
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

