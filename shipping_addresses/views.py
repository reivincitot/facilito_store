from .models import ShippingAddress
from django.shortcuts import render
from django.views.generic.list import ListView


# Create your views here.
class ShippingAddressListView(ListView):
    model = ShippingAddress()
    template_name = 'shipping_addresses/shipping_addresses.html'
    
    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
    