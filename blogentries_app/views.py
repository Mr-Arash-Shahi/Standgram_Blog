from django.shortcuts import render, get_object_or_404
from blogentries_app.models import Post, Category, Comment
from django.core.paginator import Paginator

# Create your views here.



def blogentries(request):
    post = Post.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(post, 3)
    objects_list = paginator.get_page(page_number)
    context = {
        'post': objects_list
    }

    return render(request, 'blogentries_app/blog.html', context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, post=post, user=request.user, parent_id=int(parent_id))

    context = {
        'post': post
    }
    return render(request, 'blogentries_app/post-details.html', context)


def category_list(request, pk=None):
    category = get_object_or_404(Category, id=pk)

    post = category.post_set.all()

    context = {
        'post': post
    }
    return render(request, 'blogentries_app/blog.html', context)
