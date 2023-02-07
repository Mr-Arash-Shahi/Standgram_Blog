from django.urls import path
from . import views

app_name = "blogentries_app"



urlpatterns = [
    path('blogentries_app', views.blogentries, name='blogentries_app'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('category_list/<int:pk>', views.category_list, name='category_list'),
]