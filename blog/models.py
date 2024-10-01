from email.mime import image
from time import timezone
# from turtle import title
from django.db import models
import uuid

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib.auth.models import User


class My_blog(models.Model):
    title = models.CharField(max_length=300, null=True)
    post_body = models.TextField(max_length=10000)
    image =models.ImageField(upload_to ='media/')
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    liked = models.ManyToManyField(User, related_name ='blogpost_like' )
    
    def get_total_likes(self):
        return self.likes.all().counts()
    
    def ImageUrl(self):
        try:
            image = self.image.url
            return image if image else ''
        except ValueError:
            return ''

    def __str__(self):
        return self.title +' | '+ str(self.post_date)

LIKE_CHOICES=(
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    blog =models.ForeignKey(My_blog, on_delete = models.CASCADE, null=True)
    value = models.CharField(choices =LIKE_CHOICES, default ='Like', max_length=30, null=True)

    def __str__(self):
        return str(self.blog)


class Slider(models.Model):
    title =models.CharField(max_length=40, null=True)
    description = models.TextField(max_length=1000, null=True)
    image =models.ImageField(upload_to = 'slider')

    def __str__(self):
        return self.title

class Prayers(models.Model):
    title =models.CharField(max_length=40, null=True)
    description = models.TextField(max_length=10000, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    image =models.ImageField(upload_to ='media/', null = True)
    intro=models.TextField(max_length=10000, null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_posted',]
        
class Novena(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    post_body = models.TextField(max_length=10000)
    image =models.ImageField(upload_to ='media/')
    post_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-post_date']
                
class PrayerIntro(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=10000)
    image =models.ImageField(upload_to ='media/')
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-post_date']

    
class Days(models.Model):
    day1 = models.TextField(max_length=5000, null =False, blank = False)
    day2 = models.TextField(max_length=5000, null =False, blank = False)
    day3 = models.TextField(max_length=5000, null =False, blank = False)
    day4 = models.TextField(max_length=5000, null =False, blank = False)
    day5 = models.TextField(max_length=5000, null =False, blank = False)
    day6 = models.TextField(max_length=5000, null =False, blank = False)
    day7 = models.TextField(max_length=5000, null =False, blank = False)
    day8 = models.TextField(max_length=5000, null =False, blank = False)
    day9 = models.TextField(max_length=5000, null =False, blank = False)
    novena = models.ForeignKey(Novena, on_delete=models.CASCADE, null=False, blank = False, related_name = 'daysofnovena')
    
    def __str__(self):
        return self.novena
   
class Dailyprayer(models.Model):
    title =models.CharField(max_length=50, null=False)
    prayer = models.TextField(max_length=10000, null=False)
    date_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class About_us(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=10000, null=True)
    email =models.EmailField(null=True)
    phone = models.CharField(max_length=16, null=True)


class Comment(models.Model):
    post_body = models.TextField(max_length=10000)
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    blog =models.ForeignKey(My_blog, related_name='comment', on_delete = models.CASCADE, null=True)
    # novena =models.ForeignKey(Novena, related_name='novena_comments', on_delete = models.CASCADE, null=True)


class NovenaComment(models.Model):
    post_body = models.TextField(max_length=10000)
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    # blog =models.ForeignKey(My_blog, related_name='comment', on_delete = models.CASCADE, null=True)
    novenas =models.ForeignKey(Novena, related_name='novena_comments', on_delete = models.CASCADE, null=True)

class SubscribedUser(models.Model):
    name = models.CharField(max_length =100, null=True)
    email= models.EmailField(unique =True, max_length =100)
    created_date =models.DateTimeField('Date Created', auto_now_add=True)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class NewsLetter(models.Model):
    title = models.CharField(max_length = 100, null = True)
    letter = models.TextField(max_length=10000, null=False)
    news_img=models.ImageField(upload_to ='new image/', null =True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Stationsprayers(models.Model):
    title= models.CharField(max_length =100, null=True)
    heading=models.CharField(max_length =100, null=True)
    we_ador=models.CharField(max_length =500, null=True)
    from_pro= models.TextField(max_length=20000, null=True, blank=True)
    prayer= models.TextField(max_length =10000, null=True)
    words_of_our_lord= models.TextField(max_length =10000, null=True)
    hymn=models.CharField(max_length =500, null=True) 
    
    def __str__(self):
        return self.title
class Stationofcross(models.Model):
    title= models.CharField(max_length =100, null=True)
    date =models.DateTimeField('Date Created', auto_now_add=True)
    stationimages=models.ForeignKey('StationsImages', on_delete=models.CASCADE, null = True)
    letuspray=models.ForeignKey(Stationsprayers, on_delete=models.CASCADE, null = True)
    number_of_stations = models.IntegerField(default = 0, null = True)  
    def __str__(self):
        return self.title
    
class StationsImages(models.Model):
    title =models.CharField(max_length =100, null=True)
    station_img=models.ImageField(upload_to ='station/', null =True)
    
    def __str__(self):
        return self.title
class Station_open_closing_prayer(models.Model):
    opening_prayers= models.TextField(max_length =20000, null=True)
    closing_prayers= models.TextField(max_length=20000)
    sation_intro = models.TextField(max_length=10000, null = True)
    date =models.DateTimeField(auto_now_add=True, null = True)
    # image=models.ImageField(upload_to ='station/', null =True)
    opening_prayer_image = models.ForeignKey('OpeningPrayerImages', on_delete=models.CASCADE, null = True)
    
class OpeningPrayerImages(models.Model):
    title =models.CharField(max_length =100, null=True)
    station_img=models.ImageField(upload_to ='station/', null =True)
    
    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    image =models.ImageField(upload_to ='gallery/')
    date =models.DateTimeField(auto_now_add=True, null = True)

    class Meta:
        ordering = ['-date',]

    def ImageUrl(self):
        try:
            image = self.image.url
            return image if image else ''
        except ValueError:
            return ''

    def __str__(self):
        return self.image
