from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RecipeForm, RecipeImageForm

# Create your views here.
def recipes_list(request):
    ctx = {
        "recipes" : Recipe.objects.all()
    }
    return render(request, "recipes_list.html", ctx)

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    ctx = {
        "recipe" : recipe
    }
    return render(request, "recipe_detail.html", ctx)

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe 
    form_class = RecipeForm
    success_url = reverse_lazy('ledger:recipes_list')

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_pk'] = self.kwargs['pk']
        return context
