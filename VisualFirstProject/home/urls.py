from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.landpage,name='home'),
    path('about',views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("projects",views.projects,name='projects'),
    path("congratulation",views.congratulation,name='congratulation'),
    path("api",views.api,name='api'),
    path("videodownloader",views.videodownloader,name='videodownloader')
    
]
