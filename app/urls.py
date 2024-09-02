from django.urls import path
from app import views

urlpatterns = [
    path('blogs/', views.get_blogs, name='blogs'),
    path('blogcategories/', views.api_blogscategories, name='apiBlogCategories' ),
    path('getBlogDetails/<int:blog_id>/', views.getBlogDetails, name='Blog Details' ),
    path('categoryblogs/<int:blogcategory_id>/', views.getBlogByCategory, name='apiCategoryblogs' ),
    path('project/', views.projects, name='project' ),
    path('projectdetails/<int:product_id>/', views.projectDetails, name='projectDetails' ),
    path('plantOwners/', views.create_plant_owner, name='create_plant_owner'),
    path('buyers/', views.create_buyer, name='create_buyer'),
    path('contact/', views.contact, name='contact'),
    path('calculate-irec-revenue/', views.IRECCalculatorView.as_view(), name='calculate-irec-revenue'),
]
