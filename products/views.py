from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.db.models import Q

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['message']='Listado de productos'
        return contex
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        print(contex)
        return contex

class ProductSearchListView(ListView):
    template_name='products/search.html'
    def get_queryset(self):
        filter = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        return Product.objects.filter(filter)
    def query(self):
        return self.request.GET.get('q')
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['query']= self.query 
        contex['count']= contex['product_list'].count()
        return contex

    