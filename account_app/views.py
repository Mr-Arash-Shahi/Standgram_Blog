from account_app.forms import EditForm
from account_app.models import User, Profile
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
def register_user(request):
    context = {"errors": []}

    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == "POST":
        fullname = request.POST.get('fullname')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password != password2:
            context['errors'].append('Your Password is not same')
            return render(request, 'account_app/Register.html', context)

        user = User.objects.create(fullname=fullname, password=password, email=email)
        login(request, user)
        return redirect('home_app:home')
    context = {}
    return render(request, 'account_app/Register.html', context)

def login_user(request):

    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_app:home')

    context = {}

    return render(request, 'account_app/index.html', context)

def log_out(request):
    logout(request)
    return redirect('home_app:home')

def profile(request, pk):
    user = User.objects.all()
    user.get(id=pk)

    context = {
        'user' : user
    }

    return render(request, 'account_app/profile_page.html', context)


class EditView(generic.UpdateView):
    form_class = EditForm
    template_name = 'account_app/edit_profile.html'
    success_url = reverse_lazy('home_app:home')

    def get_object(self):
        return self.request.user