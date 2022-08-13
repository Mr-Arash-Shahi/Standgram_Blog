from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/post')



    def __str__(self):
        return f"{self.title}"