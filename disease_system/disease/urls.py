from django.urls import path
from disease.views.doctors import doctors, index

urlpatterns = [
    path('', view=index, name='index'),
    path('doctors/', view=doctors, name='doctors'),
]
