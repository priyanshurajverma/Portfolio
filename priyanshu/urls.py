from priyanshu import views
from django.urls import path
from django.contrib import admin
urlpatterns = [
        path("",views.Index,name='priyanshu'),
        path("index.html",views.Index,name='priyanshu'),

    path("Contact.html",views.Contact_view,name='priyanshu'),

    path("About.html",views.About,name='priyanshu'),
    path("Services.html",views.Services,name='priyanshu'),
    path("projects.html",views.Projects,name='priyanshu')


]
