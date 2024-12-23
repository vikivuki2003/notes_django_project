from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from notes_app.models import Notes


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # forms.py
    from django import forms
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']  # Поля вашей модели
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'placeholder': 'Введите содержимое'}),
        }