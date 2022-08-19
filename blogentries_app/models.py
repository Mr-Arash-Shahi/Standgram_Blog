from account_app.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    riter = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=50, unique=True)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/post')


    def __str__(self):
        return f"{self.title}"