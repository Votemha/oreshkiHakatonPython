from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "text", "tags"]


class AdminUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class AdminUserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "email", "is_active", "is_staff", "is_superuser"]
