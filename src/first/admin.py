from django.contrib import admin

# Register your models here.
from .models import Category, RandomList

admin.site.register(Category)
admin.site.register(RandomList)