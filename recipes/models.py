
from django.db import models
from django.contrib.auth.models import User

#Post = recipe, maybe should be called "recipe"?
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ingredient1 = models.CharField(max_length=200)
    ingredient2 = models.CharField(max_length=200)