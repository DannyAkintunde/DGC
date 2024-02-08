from django.urls import path
from . import views

app_name = 'dgc_app'
urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('courses/',views.available_courses,name='courses'),
    path('services/',views.services,name='services'),
    path('news/', views.news, name='news' ),
    path('news/<str:title>',views.news_details,name='news_details'),
    path('avaliable-countries/<str:url>',views.avaliable_countries,name='avaliable_country'),
    ]