from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from disease.models import Recipe
from django.contrib import messages
from disease.forms import RecipeForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO


@login_required(login_url='login')
def patient_recipes(request: HttpRequest, user_id: int) -> HttpResponse:
    recipes = Recipe.objects.filter(user__id=user_id)
    context = {'recipes': recipes}
    return render(request, 'disease/recipe/recipe_patient.html', context)


@login_required(login_url='login')
def recipe_create(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.doctor = recipe_form.cleaned_data['doctor']
            recipe.save()
            messages.success(request, 'Ви успішно створили новий рецепт!')
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
    if request.user.id == recipe.user.id:
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
    else:
        messages.error(request, 'Ви не можете редагувати iнщi записи!')
        return redirect('profile', request.user.id)
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


@login_required(login_url='login')
def recipe_download(request: HttpRequest, recipe_id: int) -> HttpResponse:
    recipe_obj = Recipe.objects.get(id=recipe_id)

    text = [
        f"Прізвище: {recipe_obj.user.last_name}",
        "",
        f"Ім'я: {recipe_obj.user.first_name}",
        "",
        f"Лiки: {recipe_obj.pill}",
        "",
        f"Дата виписки рецепта: {recipe_obj.date_discharge.strftime('%d/%m/%Y')}",
        "",
        f"Доктор: {recipe_obj.doctor}",
    ]

    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=letter)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    pdf_canvas.setFont("Arial", 12)

    y_coordinate = 750

    for line in text:
        pdf_canvas.drawString(100, y_coordinate, line)
        y_coordinate -= 20

    pdf_canvas.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Recipe.pdf"'
    return response
