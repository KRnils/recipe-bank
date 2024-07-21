from django.db import models
from django.contrib.auth.models import User

# The core of the project, information about recipes are saved here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta():
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"

# Going with ingredients as a separate model to allow any number of ingredients to be added to a recipe.
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return "Ingredient: "+self.content()