from django.contrib import admin

# Register your models here.
from .models import Blog

@admin.register(Blog)
class BlogPostAdmin(admin.ModelAdmin):
    pass