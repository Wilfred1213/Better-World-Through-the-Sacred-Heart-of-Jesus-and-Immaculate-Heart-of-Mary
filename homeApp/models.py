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
