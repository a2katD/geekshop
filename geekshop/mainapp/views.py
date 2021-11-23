from django.shortcuts import render
import os
import json
from mainapp.models import ProductCategory, Product

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Geekshop - Товары',
    }
    context['categories'] = ProductCategory.objects.all()
    context['products'] = Product.objects.all()
    return render(request, 'mainapp/products.html', context)
