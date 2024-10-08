# Generated by Django 4.1.2 on 2024-03-19 05:05

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'blogcategory',
                'verbose_name_plural': 'blogcategories',
            },
        ),
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=256, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('more_projects', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=256, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlantOwners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=256, null=True)),
                ('project_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('project_type', models.CharField(choices=[('wind', 'wind'), ('solar', 'solar'), ('hydro', 'hydro'), ('biomass', 'biomass')], max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('cover', pyuploadcare.dj.models.ImageField()),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('image2', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('image3', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('methodologyTitle', models.CharField(max_length=200)),
                ('methodology', models.TextField(max_length=4000)),
                ('about', models.TextField(default='', max_length=4000)),
                ('location', models.CharField(max_length=200)),
                ('verifier', models.CharField(default='', max_length=200)),
                ('tag', models.CharField(max_length=200)),
                ('themeMethod', models.CharField(default='', max_length=200)),
                ('youtube_Video', embed_video.fields.EmbedVideoField()),
                ('webLink', models.URLField(default='')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('heading', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=1000, null=True)),
                ('tex2', models.TextField(blank=True, max_length=1000, null=True)),
                ('text3', models.TextField(blank=True, max_length=1000, null=True)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blogcategory')),
            ],
        ),
    ]
