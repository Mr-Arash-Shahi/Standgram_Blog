from django.urls import reverse
from django.utils.text import slugify
from account_app.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    riter = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=50, unique=True)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/post')
    slug = models.SlugField(unique=True, blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Post,self).save()

    def get_absolute_url(self):
        return reverse('blogentries_app:detail', kwargs={'slug' : self.slug})


    def __str__(self):
        return f"{self.title}"