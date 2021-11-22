from django.shortcuts import render
import os
import json

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
        'catalogs': [
            'Новинки',
            'Одежда',
            'Обувь',
            'Аксессуары',
            'Подарки',
        ],
    }
    file_path = os.path.join(MODULE_DIR, 'fixtures\\goods.json')

    with open(file_path, encoding='utf-8') as prod_load:
        context['products'] = json.load(prod_load)
    return render(request, 'mainapp/products.html', context)

