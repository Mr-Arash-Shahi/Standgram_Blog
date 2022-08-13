from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register_user(request):
    context = {"errors": []}

    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password != password2:
            context['errors'].append('Your Password is not same')
            return render(request, 'account_app/Register.html', context)

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
        login(request, user)
        return redirect('home_app:home')
    context = {}
    return render(request, 'account_app/Register.html', context)

def login_user(request):

    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_app:home')

    context = {}
    return render(request, 'account_app/index.html', context)

def log_out(request):
    logout(request)
    return redirect('home_app:home')


