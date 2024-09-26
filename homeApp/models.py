from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    CATEGORY_CHOICES = (
        ('ROSARY', 'Rosary'),
        ('PREACHING', 'Preaching'),
        ('TEACHING', 'Teaching'),
        ('NOVENA', 'Novena'),
        ('PRAYER', 'Prayer'),
        ('MUSIC', 'Music')

    )
    title = models.CharField(max_length=255, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
    
class SimilarField(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    bible_verse = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=10000, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    author= models.CharField(max_length=255, null=True, blank=True)
    year =models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class FocolarePassword(SimilarField):
    
    # def __str__(self):
    #     return self.title
    
    def ImageUrl(self):
        try:
            image = self.image.url
            return image if image else ''
        except ValueError:
            return ''

    class Meta:
        ordering = ['-posted_date',]

class Sacramental(models.Model):
    name = models.CharField(max_length=255)  # Name of the sacramental
    description = models.TextField()  # Detailed description of the sacramental
    image = models.ImageField(upload_to='sacramentals_images/', blank=True, null=True)  # Optional image of the sacramental
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def ImageUrl(self):
        try:
            image = self.image.url
            return image if image else ''
        except ValueError:
            return ''

    class Meta:
        ordering = ['name']
        verbose_name = 'Sacramental'
        verbose_name_plural = 'Sacramentals'

class SaintOfTheDay(models.Model):
    name = models.CharField(max_length=255)  # Name of the saint
    feast_day = models.DateField()  # Feast day of the saint
    biography = models.TextField()  # Short biography of the saint
    image = models.ImageField(upload_to='saints_images/', blank=True, null=True)  # Optional image of the saint
    patronage = models.CharField(max_length=255, blank=True, null=True)  # Patronage, if any
    quotes = models.TextField(blank=True, null=True)  # Famous quotes, if any
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def ImageUrl(self):
        try:
            image = self.image.url
            return image if image else ''
        except ValueError:
            return ''

    class Meta:
        ordering = ['feast_day']
        verbose_name = 'Saint of the Day'
        verbose_name_plural = 'Saints of the Day'


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(max_length=2000, blank=False, null=False)
    post_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Contact: {self.name} -- Email: {self.email} -- Read: {self.read}'
    
    class Meta:
        ordering = ['read',]