from django.contrib import admin
from .models import Category,User,Film,Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Film)
admin.site.register(Comment)