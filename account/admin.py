from django.contrib import admin
from .models import User
from main.models import Category,Film


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Film)