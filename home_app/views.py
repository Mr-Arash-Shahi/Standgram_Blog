from django.shortcuts import render
from blogentries_app.models import Post
# Create your views here.


def home(request):

    post = Post.objects.all()

    context = {
        'post' : post
    }
    return render(request, 'home_app/index.html', context)