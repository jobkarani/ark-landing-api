from django.contrib import admin

from app.models import *

# Register your models here.

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'methodologyTitle','methodology', 'location')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin )
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blogs)
admin.site.register(Offsetters)
admin.site.register(Emitters)
admin.site.register(Contact)