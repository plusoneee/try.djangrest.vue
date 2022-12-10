from django.contrib import admin

# Register your models here.
from .models import Article

# register model
admin.site.register(Article)