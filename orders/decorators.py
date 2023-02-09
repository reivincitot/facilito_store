from django.shortcuts import redirect
import shipping_addresses
from .utils import get_or_create_order
from carts.utils import get_or_create_cart
from django.contrib.auth.decorators import login_required

def validate_cart_and_order(function):
    def wrap(request, *args, **kwargs):
        cart= get_or_create_cart(request)
        
        order = get_or_create_order(cart,request)
        
        if request.user.id != order.user_id:
            return redirect('carts:cart')
        
        return function(request,cart,order, *args, **kwargs )
        
    return wrap