from django.shortcuts import render
from django.views import View
from .models import Home_page_info,Contact_info,Available_courses,About,Services_info,Available_country,New,MetaData
# Create your views here.

def meta(page_title:str,context:list)-> None:
    #context['meta'] = MetaData.objects.get(view=v)
    pass

def index(request):
    context = {
        'home_page_info':Home_page_info.objects.get(id=1),
        'c':Contact_info.objects.get(id=1),
        'p':Contact_info.objects.get(id=1).phone_numbers.all,
        'e':Contact_info.objects.get(id=1).emails.all,
        'avalable_courses':Available_courses.objects.get(id=1),
        'course':Available_courses.objects.get(id=1).course.all,
        'acs':Available_country.objects.all,
    }
    meta('index',context)
    
    return render(request,'dgc_app/index.html',context)

def about(request):
    context = {
        'c':Contact_info.objects.get(id=1),
        'p':Contact_info.objects.get(id=1).phone_numbers.all,
        'e':Contact_info.objects.get(id=1).emails.all,
        'about':About.objects.get(id=1),
        'acs':Available_country.objects.all,  
    }
    meta('about',context)
    return render(request,'dgc_app/about.html',context)

def available_courses(request):
    context = {
        'c':Contact_info.objects.get(id=1),
        'p':Contact_info.objects.get(id=1).phone_numbers.all,
        'e':Contact_info.objects.get(id=1).emails.all,
        'avalable_courses':Available_courses.objects.get(id=1),
        'course':Available_courses.objects.get(id=1).course.all,
        'acs':Available_country.objects.all,
    }
    meta('available_courses',context)
    return render(request,'dgc_app/avalable_courses.html',context)

def services(request):
    context = {
        'c':Contact_info.objects.get(id=1),
        'p':Contact_info.objects.get(id=1).phone_numbers.all,
        'e':Contact_info.objects.get(id=1).emails.all,
        's':Services_info.objects.get(id=1),
        'si':Services_info.objects.get(id=1).services.all,
        'acs':Available_country.objects.all,
    }
    meta('services',context)
    return render(request,'dgc_app/services.html',context)


def news(request):
    context = {
        'c':Contact_info.objects.get(id=1),
        'p':Contact_info.objects.get(id=1).phone_numbers.all,
        'e':Contact_info.objects.get(id=1).emails.all,
        'acs':Available_country.objects.all,
        'news':New.objects.all,
    }    
    meta('news',context) 
    return render(request,'dgc_app/news.html',context)

def news_details(request,title):
    context = {
        'c':Contact_info.objects.get(id=1),
        'p':Contact_info.objects.get(id=1).phone_numbers.all,
        'e':Contact_info.objects.get(id=1).emails.all,
        'news':New.objects.get(title=title)
    }
    meta(title,context)
    return render(request,'dgc_app/news-details.html',context)


def avaliable_countries(request,url):
    context={
        'c':Contact_info.objects.get(id=1),
        'p':Contact_info.objects.get(id=1).phone_numbers.all,
        'e':Contact_info.objects.get(id=1).emails.all,
        'ac':Available_country.objects.get(url=url),
        'acs':Available_country.objects.all,
    }
    meta(url,context)
    return render(request,'dgc_app/avalable_country.html',context)


