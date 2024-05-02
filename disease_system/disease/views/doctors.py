from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from disease.models import Doctor
from django.core.paginator import Paginator


@login_required(login_url='login')
def doctors(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    doctors = Doctor.objects.all()
    pagination = Paginator(doctors, 7)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'disease/doctors.html', context)


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})
