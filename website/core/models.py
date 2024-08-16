from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()  
    
    class Meta:
        verbose_name_plural = "Blogs"
    
    def __str__(self):
        return self.title
