from blogentries_app.models import Post, Category

def recent_post(request):
    recent_post  = Post.objects.all()[:3]
    return {'recent_post': recent_post}


def category_list(request):
    category = Category.objects.all()
    return {'category': category}
