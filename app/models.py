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
    methodologyTitle = models.CharField(max_length=200)
    methodology = models.TextField(max_length=4000)
    about = models.TextField(max_length=4000, default="")
    location = models.CharField(max_length=200)
    verifier = models.CharField(max_length=200, default="")
    tag = models.CharField(max_length=200)
    themeMethod = models.CharField(max_length=200, default="")
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

class ProjectTypeManager(models.Manager):
    def wind_type(self):
        return super(ProjectTypeManager, self).filter(project_type="wind",is_active=True)

    def solar_type(self):
        return super(ProjectTypeManager, self).filter(project_type="solar",is_active=True)
    
    def hydro_type(self):
        return super(ProjectTypeManager, self).filter(project_type="hydro",is_active=True)
    
    def biomass_type(self):
        return super(ProjectTypeManager, self).filter(project_type="biomass",is_active=True)

project_type_choice=(
    ('wind', 'wind'),
    ('solar', 'solar'),
    ('hydro', 'hydro'),
    ('biomass', 'biomass'),
)

class PlantOwners(models.Model):
    full_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=256, null=True)
    project_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100, choices=project_type_choice)
    country = models.CharField(max_length=100)

    def save_plant_owner(self):
        self.save()

    def __str__(self):
        return self.full_name
    
class Buyers(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    more_projects = models.TextField(blank=True, null=True)

    def save_emitter(self):
        self.save()

    def __str__(self):
        return self.company_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)

    def save_emitter(self):
        self.save()

    def __str__(self):
        return self.name