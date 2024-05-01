from django.urls import path
from disease.views import index

urlpatterns = [
    path('', view=index, name='index'),
]
