from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            cleaned_data["username"] = email  # username 필드에 email 을 설정
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]  # email → username
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

