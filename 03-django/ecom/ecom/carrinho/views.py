from django.http import HttpResponse
from django.shortcuts import render

from carrinho.models import Product


def hello_world_view(request):
    return HttpResponse('Olá, mundo!')


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'carrinho/product_list.html',
                  {'products': products})
