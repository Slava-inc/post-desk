from django.urls import path
from .views import IndexView, MessageCreate
from article.views import message_create, update


urlpatterns = [
    path('', IndexView.as_view()),
    # path('message/', MessageCreate.as_view(), name='message_create')
    path('message/<int:pk>', update, name='update')
]