from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario',max_length=50, min_length=4, required=True, widget=forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Username'}))
    email = forms.EmailField (required=True, widget=forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'example@gmail.com'}))
    password = forms.CharField(label='Contraseña',required=True, widget=forms.PasswordInput(attrs={'class':'form-control','id':'password'}))
    password2 = forms.CharField(label='Confirmar contraseña' ,required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'Confirmar password'}))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists(): 
            raise forms.ValidationError('El nombre de usuario ya se encuentra en uso')
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists(): 
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'La contraseña no coincide')
        