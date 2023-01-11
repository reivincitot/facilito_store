from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=4, required=True)
    email = forms.EmailField (required=True)
    password = forms.CharField(required=True)