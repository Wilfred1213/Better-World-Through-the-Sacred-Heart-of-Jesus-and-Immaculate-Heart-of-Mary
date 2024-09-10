from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Dailyprayer, SubscribedUser, NewsLetter,Gallery, My_blog, Novena, PrayerIntro, Prayers
from homeApp.models import FocolarePassword

# @receiver(post_save, sender=FocolarePassword)
# def send_daily_password_emails_handler(sender, instance, created, **kwargs):
#     if created:
#         subscribed_users = SubscribedUser.objects.all()
#         email_subject = 'Sacred Heart of Jesus - Focolare Daily Password'
#         email_template = 'blog/daily_password_email.html'
#         context = {
#             'dailypass': instance
#             }
#         html_message = render_to_string(email_template, context)
#         plain_message = strip_tags(html_message)
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
        subscribed_users = SubscribedUser.objects.all()
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
@receiver(post_save, sender=FocolarePassword)
def gallery_image_handler(sender, instance, created, **kwargs):
    if created and instance.image:
        passwordimage = instance.image
        gallery = Gallery(image = passwordimage)
        gallery.save()

@receiver(post_save, sender=My_blog)
def gallery_image_blog_handler(sender, instance, created, **kwargs):
    if created and instance.image:
        blogimage = instance.image
        gallery = Gallery(image = blogimage)
        gallery.save()

@receiver(post_save, sender=Novena)
def gallery_image_novena_handler(sender, instance, created, **kwargs):
    if created and instance.image:
        novenaimage = instance.image
        gallery = Gallery(image = novenaimage)
        gallery.save()

@receiver(post_save, sender=PrayerIntro)
def gallery_image_prayer_intro_handler(sender, instance, created, **kwargs):
    if created and instance.image:
        prayerIntroimage = instance.image
        gallery = Gallery(image = prayerIntroimage)
        gallery.save()

@receiver(post_save, sender=Prayers)
def gallery_image_prayers_handler(sender, instance, created, **kwargs):
    if created and instance.image:
        prayerimage = instance.image
        gallery = Gallery(image = prayerimage)
        gallery.save()


    