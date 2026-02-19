from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe 
    inlines = [RecipeIngredientInline]

    search_fields = ('name', )
    list_display = ('name', )

admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)