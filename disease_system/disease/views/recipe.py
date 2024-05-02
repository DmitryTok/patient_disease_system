from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from disease.models import Recipe
from django.contrib import messages
from disease.forms import RecipeForm


@login_required(login_url='login')
def patient_recipes(request: HttpRequest, user_id: int) -> HttpResponse:
    recipes = Recipe.objects.filter(user__id=user_id)
    context = {'recipes': recipes}
    return render(request, 'disease/recipe/recipe_patient.html', context)


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
        return redirect('profile', request.user.id)
    else:
        recipe_form = RecipeForm()
    context = {'recipe_form': recipe_form}
    return render(request, 'disease/recipe/recipe_create.html', context)


@login_required(login_url='login')
def recipe_edit(
    request: HttpRequest, recipe_id: int
) -> HttpResponse | HttpResponseRedirect:
    is_edit = True
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
            return redirect('profile', request.user.id)
    else:
        recipe_form = RecipeForm(instance=recipe)
    context = {'recipe_form': recipe_form, 'is_edit': is_edit}
    return render(request, 'disease/recipe/recipe_create.html', context)


@login_required(login_url='login')
def recipe_delete(request: HttpRequest, recipe_id: int) -> HttpResponse:
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user.id == recipe.user.id:
        recipe.delete()
        messages.success(request, ('Рецепт успішно видалено!'))
        return redirect('profile', request.user.id)
    else:
        messages.error(
            request, ('Ви не можете видалити рецепт іншого користувача!')
        )
        return redirect('profile', request.user.id)
