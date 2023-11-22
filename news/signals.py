from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from .models import PostCategory
from .tasks import mailing_newpost



@receiver(m2m_changed, sender=PostCategory)
def postcategory_created(sender, instance,pk_set, **kwargs):
    if kwargs['action'] == 'post_add':
        print(instance.id)
        print(instance.heading)
        mailing_newpost(instance.id)


        # catigories = instance.category.all()
        # subscribers : list[str] = []
        #
        # # for category in catigories:
        #     subscribers += User.objects.filter(subscriptions__category=category).values_list('email', flat=True)
        #
        #
        # subject = f'Новая публикаци в категории {instance.category}'
        #
        # text_content = (
        # f'Заголовок: {instance.heading}\n'
        # f'Автор: {instance.autor}\n\n'
        # f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}'
        # )
        # html_content = (
        # f'Заголовок: {instance.heading}<br>'
        # f'Автор: {instance.autor}<br><br>'
        # f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        # f'Ссылка на публикацию</a>'
        # )
        # # mailing_newpost.delay(subscribers, subject, text_content, html_content)
        # for email in subscribers:
        #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
        #     msg.attach_alternative(html_content, "text/html")
        #     msg.send()
