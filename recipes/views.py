from django.http import Http404
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from . models import Recipe, Category


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    
    
def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    
    if not recipes:
        raise Http404('Pagina não encontrada')
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'Categoria | {recipes.first().category.name}'
    })


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
    
    

def teste(request):
    return render(request, 'recipes/pages/teste.html')