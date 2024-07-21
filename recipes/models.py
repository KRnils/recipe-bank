
from django.db import models
from django.contrib.auth.models import User

#
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta():
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return "Ingredient: "+self.content()