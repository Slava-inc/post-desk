from django.urls import path
from .views import IndexView, MessageCreate


urlpatterns = [
    path('', IndexView.as_view()),
    path('message/', MessageCreate.as_view(), name='message_create')
]