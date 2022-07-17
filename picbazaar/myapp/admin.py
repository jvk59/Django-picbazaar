from django.contrib import admin
#1.
from .models import *
# Register your models here.
#1.
admin.site.register(Category)
admin.site.register(Image)

