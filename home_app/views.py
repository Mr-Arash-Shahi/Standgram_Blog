from django.shortcuts import render
from blogentries_app.models import Post
# Create your views here.


def home(request):

    post = Post.objects.all()
    recent_post = Post.objects.all()[:3]

    context = {
        'post' : post,
        'recent_post' : recent_post
    }
    return render(request, 'home_app/index.html', context)


