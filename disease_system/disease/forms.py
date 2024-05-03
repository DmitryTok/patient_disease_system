from django import forms
from django.db.models import QuerySet
import typing as t
from django.core.exceptions import ValidationError
import datetime

from disease.models import Note, Recipe


class NoteForm(forms.ModelForm):
    diagnosis = forms.CharField(
        label='Діагноз',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Діагноз'}
        ),
    )
    treatment = forms.CharField(
        label='Лікування',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Лікування'}
        ),
    )
    complaint = forms.CharField(
        label='Скарги',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Скарги'}
        ),
    )

    class Meta:
        model = Note
        fields = '__all__'
        exclude = ('user',)
        labels = {'doctor': 'Лікар'}


class RecipeForm(forms.ModelForm):
    pill = forms.CharField(
        label='Ліки',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ліки'}
        ),
    )
    date_discharge = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Дата виписки рецепта',
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'class': 'form-control', 'placeholder': '(дд/мм/рррр)'},
        ),
    )

    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('user',)
        labels = {'doctor': 'Лікар'}

    def clean_date_discharge(self):
        date = self.cleaned_data['date_discharge']
        if date.month > 12:
            raise ValidationError("Месяц не может быть больше 12.")
        return date
