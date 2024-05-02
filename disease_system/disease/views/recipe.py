from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from disease.models import Recipe
from django.contrib import messages
from disease.forms import RecipeForm


@login_required(login_url='login')
def patient_recipes(request: HttpRequest) -> HttpResponse:
    pass


@login_required(login_url='login')
def recipe_detail(request: HttpRequest) -> HttpResponse:
    pass


@login_required(login_url='login')
def recipe_create(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    recipe_form = RecipeForm(request.POST or None)
    if request.method == 'POST':
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.doctor = recipe_form.cleaned_data['doctor']
            recipe.save()
            messages.success(
                request,
                ('Ви успішно створили новий рецепт!'),
            )
        return redirect('index')
    else:
        recipe_form = RecipeForm()
    context = {'recipe_form': recipe_form}
    return render(request, 'disease/recipe/recipe_create.html', context)


@login_required(login_url='login')
def recipe_edit(
    request: HttpRequest, recipe_id: int
) -> HttpResponse | HttpResponseRedirect:
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, instance=recipe)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.doctor = recipe_form.cleaned_data['doctor']
            messages.success(
                request,
                ('Ви успішно оновили рецепт!'),
            )
            return redirect('index')
    else:
        recipe_form = RecipeForm(instance=recipe)
    context = {'recipe_form': recipe_form}
    return render(request, 'disease/recipe/recipe_edit.html', context)


@login_required(login_url='login')
def recipe_delete(request: HttpRequest) -> HttpResponse:
    pass
