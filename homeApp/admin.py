from django.contrib import admin
from . models import Category, FocolarePassword, Contact, Sacramental, SaintOfTheDay

# # Register your models here.
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(FocolarePassword)
admin.site.register(Sacramental)
admin.site.register(SaintOfTheDay)
