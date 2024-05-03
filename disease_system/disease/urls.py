from django.urls import path
from disease.views.doctors import doctors, index
from disease.views.notes import (
    note_create,
    patient_notes,
    note_edit,
    note_delete,
    note_download,
)
from disease.views.recipe import (
    recipe_create,
    recipe_edit,
    patient_recipes,
    recipe_delete,
    recipe_download,
)

urlpatterns = [
    path('', view=index, name='index'),
    path('doctors/', view=doctors, name='doctors'),
    path('note_create/', view=note_create, name='note_create'),
    path('note_edit/<int:note_id>', view=note_edit, name='note_edit'),
    path('note_delete/<int:note_id>', view=note_delete, name='note_delete'),
    path(
        'note_download/<int:note_id>', view=note_download, name='note_download'
    ),
    path(
        'patient_notes/<int:user_id>', view=patient_notes, name='patient_notes'
    ),
    path('recipe_create/', view=recipe_create, name='recipe_create'),
    path('recipe_edit/<int:recipe_id>', view=recipe_edit, name='recipe_edit'),
    path(
        'patient_recipes/<int:user_id>',
        view=patient_recipes,
        name='patient_recipes',
    ),
    path(
        'recipe_delete/<int:recipe_id>',
        view=recipe_delete,
        name='recipe_delete',
    ),
    path(
        'recipe_download/<int:recipe_id>',
        view=recipe_download,
        name='recipe_download',
    ),
]
