from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect



def index(request):
    return render(request,'index.html',{
        'message': 'Listado de productos',
        'title': 'Productos',
        'products':[
            {'title': 'Playera','price':5,'stock': True},
            {'title': 'Camisa','price':7,'stock': True},
            {'title': 'Mochila','price':20,'stock': True},
            {'title': 'Mitones','price':10,'stock': False}
            ]
    })
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request,'Usuario o contraseña no validos')
        
    return render(request,'users/login.html',{
        
    })
def logout_view(request):
    logout(request)
    messages.success(request,'Sesión cerrada exitosamente')
    return redirect('login')