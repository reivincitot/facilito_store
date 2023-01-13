from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['message']='Listado de productos'
        print(contex)
        return contex
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        print(contex)
        return contex
