from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blog_item = Blog.objects.all()
    return render(request , "index.html" , {"Blogs": blog_item })