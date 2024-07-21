from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe

# Create your views here.


class RecipeList(generic.ListView):
    model = Recipe
    template_name = "recipes/index.html"
    queryset = Recipe.objects.all()
    paginate_by = 2


class RecipeDetail(generic.DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context