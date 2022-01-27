from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

import json
import os

from django.views.generic import DetailView

from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    context = {
        'title': 'DailySushi', }
    return render(request, 'mainapp/index.html', context)


def action(request):
    context = {
        'title': 'DailySushi | Акции', }
    return render(request, 'mainapp/action.html', context)

def contacts(request):
    context = {
        'title': 'DailySushi | Контакты', }
    return render(request, 'mainapp/contacts.html', context)


def products(request, id_category=None, page=1):
    context = {
        'title': 'DailySushi | Каталог',
    }

    if id_category:
        products = Product.objects.filter(category_id=id_category).select_related('category')
    else:
        products = Product.objects.all().select_related('category')

    paginator = Paginator(products, per_page=9)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

