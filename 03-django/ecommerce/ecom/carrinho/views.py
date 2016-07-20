from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from carrinho.forms import LoginForm
from carrinho.models import Product


def hello_world_view(request):
    return HttpResponse('Olá, mundo!')


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        # pega dados do form e autentica usuário
        pass


def product_list_view(request):
    products = Product.objects.filter(active=True)
    return render(request, 'carrinho/product_list.html',
                  {'products': products})


def product_detail_view(request, key):
    product = get_object_or_404(Product, pk=key, active=True)
    return render(request, 'carrinho/product_detail.html',
                  {'product': product})
