from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from email import message
from django.conf import settings
from ..desk.models import Message, Article
from django.contrib.auth.models import User

def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'desk_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/article/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title, # Заголовок
        body='', # Тело пустое т.к. используем шаблон
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=list(subscribers), # Кому отправляем
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()