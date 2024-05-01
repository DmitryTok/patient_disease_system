from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "Ім'я"}
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Прізвище'}
        ),
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs[
            'placeholder'
        ] = "Ім'я користувача"
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted"><small>Вимагається. 150 символів або менше. Лише літери, цифри та @/./+/-/_.</small></span>'
        )

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small"><li>Ваш пароль не може бути дуже схожим на вашу іншу особисту інформацію.</li><li>Ваш пароль має містити щонайменше 8 символів.</li><li>Ваш пароль не може бути загальновживаним паролем. </li><li>Ваш пароль не може бути повністю цифровим.</li></ul>'
        )

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs[
            'placeholder'
        ] = 'Підтвердьте пароль'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted"><small>Для підтвердження введіть той самий пароль, що й раніше.</small></span>'
        )
