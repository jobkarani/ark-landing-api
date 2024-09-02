from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'slug', 'cover', 'image', 'image2', 'image3', 'methodologyTitle','methodology', 'about', 'location', 'verifier', 'tag', 'themeMethod', 'youtube_Video', 'webLink']

class BlogsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='blog_category.name')
    category_slug = serializers.CharField(source='blog_category.slug')
    category_id = serializers.IntegerField(source='blog_category.id')
    class Meta:
        model = Blogs
        fields = ['id', 'image', 'heading', 'created_at', 'text','tex2','text3','category_name','category_slug', 'category_id']

class BlogCategorySerializer(serializers.ModelSerializer):
    blogs = BlogsSerializer(many=True, read_only=True)
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug', 'blogs']

class PlantOwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantOwners
        fields = ['full_name', 'company', 'email', 'project_name', 'phone', 'project_type', 'country']

    def create(self, validated_data):
        return PlantOwners.objects.create(**validated_data)
    
class Buyerserializer(serializers.ModelSerializer):
    class Meta:
        model = Buyers
        fields = ['id', 'company_name', 'email', 'phone', 'project_type', 'country', 'more_projects']

    def create(self, validated_data):
        return Buyers.objects.create(**validated_data)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'subject', 'message']

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

class SolarPlantInputSerializer(serializers.Serializer):
    capacity_mw = serializers.FloatField(min_value=0.0)
    average_monthly_mwh = serializers.FloatField(min_value=0.0)

    def calculate_annual_revenue(self):
        data = self.validated_data
        # Assuming the base price of IREC is $3 per I-REC
        price_per_irec = 3.0
        
        # Calculate annual MWh from monthly MWh
        annual_mwh = data['average_monthly_mwh'] * 12
        
        # Calculate the number of I-RECs (1 I-REC = 1000 MWh)
        annual_irecs = annual_mwh / 1000
        
        # Calculate annual revenue from I-RECs
        annual_revenue = annual_irecs * price_per_irec
        
        return annual_revenue