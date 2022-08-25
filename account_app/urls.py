from django.urls import path
from . import views
from .views import EditView

app_name = 'account_app'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.log_out, name='logout'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('edit_profile', EditView.as_view(), name='edit'),
]