from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from disease.models import Doctor


@login_required(login_url='login')
def doctors(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'disease/doctors.html', context)


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})
