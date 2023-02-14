from django.urls import path
from . import views

app_name='billing_profiles'

urlpatterns = [
    path('nuevi', views.create,name='create')
]
