from django.urls import path
from . import views

app_name = "blogentries_app"



urlpatterns = [
    path('blogentries', views.blogentries, name='blogentries'),
]