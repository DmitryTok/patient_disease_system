from django.shortcuts import render, redirect, get_object_or_404
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
def note_create(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
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
def note_edit(request: HttpRequest, note_id: int) -> HttpResponse:
    is_edit = True
    note = get_object_or_404(Note, pk=note_id)
    if request.user.id == note.user.id:
        if request.method == 'POST' and request.user.id == note.user.id:
            note_form = NoteForm(request.POST, instance=note)
            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.user = request.user
                note.doctor = note_form.cleaned_data['doctor']
                messages.success(
                    request,
                    ('Ви успішно оновили запис!'),
                )
                return redirect('profile', request.user.id)
        else:
            note_form = NoteForm(instance=note)
    else:
        messages.error(request, 'Ви не можете редагувати iнщi записи!')
        return redirect('profile', request.user.id)
    context = {'note_form': note_form, 'is_edit': is_edit}
    return render(request, 'disease/note/note_create.html', context)


@login_required(login_url='login')
def note_delete(
    request: HttpRequest, note_id: int
) -> HttpResponse | HttpResponseRedirect:
    note = get_object_or_404(Note, pk=note_id)
    if request.user.id == note.user.id:
        note.delete()
        messages.success(request, ('Запис успішно видалено!'))
        return redirect('profile', request.user.id)
    else:
        messages.error(
            request, ('Ви не можете видалити запис іншого користувача!')
        )
        return redirect('profile', request.user.id)
