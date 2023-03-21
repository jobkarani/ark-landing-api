from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
from  embed_video.fields  import  EmbedVideoField
# Create your models here.
    
class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    cover = ImageField( manual_crop="")
    image = ImageField( manual_crop="") 
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    methodologyTitle = models.CharField(max_length=200, unique=True)
    methodology = models.TextField(max_length=4000)
    about = models.TextField(max_length=4000, default="")
    location = models.CharField(max_length=200, unique=True)
    tag = models.CharField(max_length=200, unique=True)
    youtube_Video = EmbedVideoField()
    webLink = models.URLField(max_length = 200, default="")
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'blogcategory'
        verbose_name_plural = 'blogcategories'

    def get_url(self):
        return reverse('blogs_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Blogs(models.Model):
    image = ImageField( manual_crop="")
    heading = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000, blank=False, null=True)
    tex2 = models.TextField(max_length=1000, blank=True, null=True)
    text3 = models.TextField(max_length=1000, blank=True, null=True)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading