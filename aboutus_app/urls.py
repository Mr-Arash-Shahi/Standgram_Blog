from django.urls import path
from . import views

app_name = "aboutus_app"



urlpatterns = [
    path('about_us', views.abuotus, name='aboutus'),
]