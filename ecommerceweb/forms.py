from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer  # Specifies that this form is for the `Customer` model
        fields = ['text', 'photo']  # Limits the fields to `text` and `photo`

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter text'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control'})

class UserRegistrationForm(UserCreationForm):  # Corrected inheritance from UserCreationForm
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
