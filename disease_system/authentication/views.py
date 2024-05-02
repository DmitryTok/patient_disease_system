from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from authentication.models import Patient


@login_required(login_url='login')
def profile(
    request: HttpRequest, patient_id: int
) -> HttpResponse | HttpResponseRedirect:
    if request.user.id == patient_id:
        patient = get_object_or_404(Patient, pk=patient_id)
        context = {'patient': patient}
        return render(request, 'authentication/profile.html', context)
    else:
        messages.error(
            request, ('Ви не можете змінювати та переглядати інші профілі!')
        )
        return redirect('profile', request.user.id)


def register(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            birth_date = form.cleaned_data['birth_date']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']

            Patient.objects.create(
                id=user.id,
                user=user,
                birth_date=birth_date,
                height=height,
                weight=weight,
            )

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Ви успішно зареєструвалися!'))
            return redirect('index')
    context = {'form': form}

    return render(request, 'authentication/register.html', context)


def login_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Ви увійшли в систему!')
            return redirect('index')
        else:
            messages.error(
                request, ('Під час входу сталася помилка. Повторіть спробу!')
            )
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})


def logout_user(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    messages.success(request, ('Ви успішно вийшли з системи!'))
    return redirect('index')
