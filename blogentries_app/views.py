from django.shortcuts import render
from blogentries_app.models import Post
# Create your views here.



def blogentries(request):

    post = Post.objects.all()

    context = {
        'post' : post
    }

    return render(request, 'blogentries/blog.html', context)