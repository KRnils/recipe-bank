from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipeList(generic.ListView):
    """
    Recipe list is the starting page of the website and shows a list of all recipes in the database.
    """
    model = Recipe
    template_name = "recipes/index.html"
    queryset = Recipe.objects.all()
    paginate_by = 4


class RecipeDetail(generic.DetailView):
    """
    Recipe detail view shows the author, creation date, text and ingredients of a recipe.
    """
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context