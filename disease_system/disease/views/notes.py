from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from disease.models import Note
from django.contrib import messages
from disease.forms import NoteForm


@login_required(login_url='login')
def patient_notes(request: HttpRequest, user_id: int) -> HttpResponse:
    notes = Note.objects.filter(user__id=user_id)
    context = {'notes': notes}
    return render(request, 'disease/note/note_patient.html', context)


@login_required(login_url='login')
def note_details(request: HttpRequest) -> HttpResponse:
    pass


@login_required(login_url='login')
def note_create(request: HttpRequest) -> HttpResponse:
    note_form = NoteForm(request.POST or None)
    if request.method == 'POST':
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.user = request.user
            note.doctor = note_form.cleaned_data['doctor']
            note.save()
            messages.success(
                request,
                ('Ви успішно створили новий запис!'),
            )
        return redirect('index')
    else:
        note_form = NoteForm()
    context = {'note_form': note_form}
    return render(request, 'disease/note/note_create.html', context)


@login_required(login_url='login')
def note_edit(request: HttpRequest) -> HttpResponse:
    pass


@login_required(login_url='login')
def note_delete(request: HttpRequest) -> HttpResponse:
    pass
