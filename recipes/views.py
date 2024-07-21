from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe

# Create your views here.
class RecipeList(generic.ListView):
    template_name = "recipes/index.html"
    queryset = Recipe.objects.all()
    paginate_by = 4