from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    class Meta:
        verbose_name_plural = "Blogs"
    
    def __str__(self):
        return self.title
