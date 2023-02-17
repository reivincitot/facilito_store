import json
import stripe
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from billing_profiles.servidor import calculate_order_amount
# Create your views here.

stripe.api_key = "sk_test_51MbUhqI8OQstmejQe6brFtNMKSM60PSimt8VYQUJC4NhwLcpYSocuhqx3tpMV12wmvJrVIdtdfwSRKaPEDjD0oTQ006FiLy4HU"

@login_required(login_url='login')
def create(request):
    return render(request,'billing_profiles/create.html',{
        
    })
    