from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from carrinho.forms import LoginForm, PersonCreateForm
from carrinho.models import Product


def hello_world_view(request):
    return HttpResponse('Olá, mundo!')


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Invalid data')

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,
                            password=password)
        if not user:
            return HttpResponse('Invalid username and/or password')

        login(request, user)
        return HttpResponseRedirect(reverse('home'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def person_create_view(request):
    if request.method == "GET":
        form = PersonCreateForm()
        return render(request, 'carrinho/person_create.html', {'form': form})
    elif request.method == "POST":
        pass


def product_list_view(request):
    products = Product.objects.filter(active=True)
    return render(request, 'carrinho/product_list.html',
                  {'products': products})


def product_detail_view(request, key):
    product = get_object_or_404(Product, pk=key, active=True)
    return render(request, 'carrinho/product_detail.html',
                  {'product': product})
