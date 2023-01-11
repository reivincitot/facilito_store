from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=4, required=True, widget=forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Username'}))
    email = forms.EmailField (required=True, widget=forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'example@gmail.com'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control','id':'password'}))