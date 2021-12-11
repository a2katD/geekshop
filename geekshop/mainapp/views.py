from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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


def products(request, id_category=None, page=1):
    context = {
        'title': 'Geekshop - Товары',
    }
    if id_category:
        products = Product.objects.filter(category_id=id_category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)
