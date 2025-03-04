from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
   title = models.CharField(max_length=200, unique=True)
   slug = models.SlugField(max_length=200, unique=True)
   content = MarkdownxField()  
   banner_image = models.ImageField(upload_to='banners/', null=True, blank=True)  
   created_on = models.DateTimeField(auto_now_add=True)


   class Meta:
       ordering = ['-created_on']


   def __str__(self):
       return self.title


   def formatted_markdown(self):
       return markdownify(self.content) 