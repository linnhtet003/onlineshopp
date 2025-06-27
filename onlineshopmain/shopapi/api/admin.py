from django.contrib import admin
from .models import CustomUser,Categories,NeworPopular,Products,Review

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Categories)
admin.site.register(NeworPopular)
admin.site.register(Products)
admin.site.register(Review)