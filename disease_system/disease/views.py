from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})
