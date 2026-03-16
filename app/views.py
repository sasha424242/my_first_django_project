from django.shortcuts import render
from app.models import product

def index(request):
    products = product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'app/index.html', context)
