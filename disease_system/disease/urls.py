from django.urls import path
from disease.views.doctors import doctors, index
from disease.views.notes import note_create, patient_notes
from disease.views.recipe import recipe_create

urlpatterns = [
    path('', view=index, name='index'),
    path('doctors/', view=doctors, name='doctors'),
    path('note_create/', view=note_create, name='note_create'),
    path(
        'patient_notes/<int:user_id>', view=patient_notes, name='patient_notes'
    ),
    path('recipe_create/', view=recipe_create, name='recipe_create'),
]
