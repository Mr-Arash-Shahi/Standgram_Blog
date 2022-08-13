from django.shortcuts import render

# Create your views here.


def abuotus(request):
    return render(request, "aboutus_app/about.html", {})