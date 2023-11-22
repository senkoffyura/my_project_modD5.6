from celery import shared_task
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from NewsPaper import settings
from news.models import Post, Subscription

import datetime


@shared_task
def mailing_newpost(id):

    instance = Post.objects.get(id=id)

    catigories = instance.category.all()
    subscribers: list[str] = []

    for category in catigories:
        subscribers += User.objects.filter(subscriptions__category=category).values_list('email', flat=True)

    subject = f'Новая публикаци в категории {instance.category}'

    text_content = (
        f'Заголовок: {instance.heading}\n'
        f'Автор: {instance.autor}\n\n'
        f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Заголовок: {instance.heading}<br>'
        f'Автор: {instance.autor}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на публикацию</a>'
    )

    for email in subscribers:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

@shared_task
def action_mailing():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_creates__gte=last_week)
    categories = set(posts.values_list('category__id', flat=True))
    subscribers = set(Subscription.objects.filter(category__in=categories).values_list('user__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Публикации за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()
