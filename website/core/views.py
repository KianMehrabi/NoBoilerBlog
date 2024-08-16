from django.shortcuts import render
from .models import Blog
from django.http import HttpResponseNotFound

# Create your views here.
def index(request , *args , **kwargs):
    blog_item = Blog.objects.all()
    return render(request , "index.html" , {"Blogs": blog_item })

def individual_blog(request , id):
    try:
        blog_item = Blog.objects.get(id = id)
    except:
        print("can not found the data")
        return HttpResponseNotFound("did not found the page you were looking for")
    return render(request , "blog.html" , {"Blog": blog_item })
