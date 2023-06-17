from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Dailyprayer, SubscribedUser, NewsLetter

# @receiver(post_save, sender=Dailyprayer)
# def send_daily_prayer_emails_handler(sender, instance, created, **kwargs):
#     if created:
#         # Get the list of subscribed users
#         subscribed_users = SubscribedUser.objects.all()

#         # Render the email template with the daily prayer details
#         email_subject = 'Better World Through the Sacred Heart of Jesus and Immaculate Heart of Mary'
#         email_template = 'blog/daily_prayer_email.html'
#         context = {'dailyprayer': instance}
#         html_message = render_to_string(email_template, context)
#         plain_message = strip_tags(html_message)

#         # Send email to each subscribed user
#         for user in subscribed_users:
#             send_mail(
#                 email_subject,
#                 plain_message,
#                 'mathiaswilfred7@yahoo.com',
#                 [user.email],
#                 html_message=html_message
#             )


@receiver(post_save, sender=NewsLetter)
def send_news_letter_emails_handler(sender, instance, created, **kwargs):
    if created:
        # Get the list of subscribed users
        subscribed_users = SubscribedUser.objects.all()

        # Render the email template with the daily prayer details
        email_subject = 'Better World Through the Sacred Heart of Jesus and Immaculate Heart of Mary'
        email_template = 'blog/news_letter_email.html'
        context = {'message': instance}
        html_message = render_to_string(email_template, context)
        plain_message = strip_tags(html_message)

        # Send email to each subscribed user
        for user in subscribed_users:
            send_mail(
                email_subject,
                plain_message,
                'mathiaswilfred7@yahoo.com',
                [user.email],
                html_message=html_message
            )
