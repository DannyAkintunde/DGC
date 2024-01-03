# Generated by Django 4.2.4 on 2024-01-03 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Home_page_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('description1', models.TextField(blank=True, max_length=700, null=True)),
                ('description2', models.TextField(blank=True, max_length=700, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/assets/img')),
            ],
        ),
        migrations.CreateModel(
            name='Phone_numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Social_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=700, null=True)),
                ('services', models.ManyToManyField(blank=True, null=True, to='dgc_app.services')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('tag', models.CharField(max_length=100)),
                ('descripion', models.TextField(blank=True, null=True)),
                ('short_descripion', models.TextField()),
                ('headline', models.CharField(max_length=100)),
                ('image', models.ManyToManyField(blank=True, null=True, to='dgc_app.news_image')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=3)),
                ('list_id', models.IntegerField(unique=True)),
                ('ordered_list', models.BooleanField()),
                ('schools', models.ManyToManyField(to='dgc_app.school')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('emails', models.ManyToManyField(blank=True, null=True, to='dgc_app.email')),
                ('phone_numbers', models.ManyToManyField(blank=True, null=True, to='dgc_app.phone_numbers')),
            ],
        ),
        migrations.CreateModel(
            name='Available_courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=300)),
                ('course', models.ManyToManyField(blank=True, null=True, to='dgc_app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Available_country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('nav_title', models.CharField(max_length=100)),
                ('institution', models.ManyToManyField(to='dgc_app.institution')),
            ],
        ),
    ]
