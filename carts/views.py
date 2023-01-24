from django.shortcuts import render

# Create your views here.
def cart(request):
    #crear una sesion
    #request.session['cart_id'] = '123' # la sesion es un diccionario 
    
    #obtener el valor de una sesion
    valor = request.session.get('cart_id')
    print(valor)
    
    #eliminar una sesion
    request.session['cart_id'] = None
    
    return render(request,'carts/cart.html',{
        
    })