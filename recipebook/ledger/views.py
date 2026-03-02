from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeIngredient
#from django.contrib.auth.decorators import login_required

# Create your views here.
def recipes_list(request):
    ctx = {
        "recipes" : Recipe.objects.all()
    }
    return render(request, "recipes_list.html", ctx)

#@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    ctx = {
        "recipe" : recipe
    }
    return render(request, "recipe_detail.html", ctx)