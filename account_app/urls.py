from django.urls import path
from . import views


app_name = 'account_app'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.log_out, name='logout'),
]