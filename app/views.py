from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# from simple_mail.mail import send_mail

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


# Create your views here

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['GET',])
def projects(request):
    if request.method == "GET":
        products = Project.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = ProjectSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def projectDetails(request, product_id):
    if request.method == "GET":
        product= Project.objects.filter(id = product_id)
        serializer = ProjectSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_blogs(request):
    if request.method == "GET":
        blogs = Blogs.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def api_blogscategories(request):
    if request.method == "GET":
        blogcategories = BlogCategory.objects.all()
        serializer = BlogCategorySerializer(blogcategories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getBlogDetails(request, blog_id):
    if request.method == "GET":
        blogs= Blogs.objects.filter(id = blog_id)
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getBlogByCategory(request, blogcategory_id):
    if request.method == "GET":
        blogcategory = get_object_or_404(BlogCategory, id=blogcategory_id)
        blogs = Blogs.objects.filter(blog_category=blogcategory)
        serializer =BlogsSerializer(blogs, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_plant_owner(request):
    if request.method == "POST":
        serializer = PlantOwnersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def create_buyer(request):
    if request.method == "POST":
        serializer =Buyerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def contact(request):
    if request.method == "POST":
        serializer =ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class IRECCalculatorView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SolarPlantInputSerializer(data=request.data)
        if serializer.is_valid():
            annual_revenue = serializer.calculate_annual_revenue()
            return Response({'annual_revenue': annual_revenue}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)