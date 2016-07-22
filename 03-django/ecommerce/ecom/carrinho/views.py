from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DetailView, ListView

from carrinho.forms import LoginForm, PersonCreateForm
from carrinho.models import Person, Product


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


class PersonCreateView(CreateView):
    model = Person
    template_name = 'carrinho/person_create.html'
    form_class = PersonCreateForm

    def form_valid(self, form):
        person = form.save(commit=False)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        password_check = form.cleaned_data['password_check']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']

        if password != password_check:
            return HttpResponse('Confirmação de senha inválida')

        user = User.objects.create(username=username, password=password,
                                   email=email, first_name=first_name,
                                   last_name=last_name)

        person.user = user
        person.save()
        return HttpResponseRedirect(reverse('login'))


def person_create_view(request):
    if request.method == "GET":
        form = PersonCreateForm()
        return render(request, 'carrinho/person_create.html', {'form': form})
    elif request.method == "POST":
        form = PersonCreateForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Invalid data')

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        password_check = form.cleaned_data['password_check']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        street = form.cleaned_data['address_street']
        number = form.cleaned_data['address_number']
        cep = form.cleaned_data['address_cep']
        city = form.cleaned_data['address_city']
        state = form.cleaned_data['address_state']

        if password != password_check:
            return HttpResponse('Confirmação de senha inválida')

        user = User(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
        user.save()

        Person.objects.create(user=user, address_street=street,
                              address_number=number, address_cep=cep,
                              address_state=state, address_city=city)

        return HttpResponseRedirect(reverse('login'))


class ProductListView(ListView):
    model = Product
    template_name = 'carrinho/product_list.html'
    queryset = Product.objects.filter(active=True)


def product_list_view(request):
    products = Product.objects.filter(active=True)
    return render(request, 'carrinho/product_list.html',
                  {'products': products})


class ProductDetailView(DetailView):
    product = Product
    template_name = 'carrinho/product_detail.html'
    queryset = Product.objects.filter(active=True)


def product_detail_view(request, key):
    product = get_object_or_404(Product, pk=key, active=True)
    return render(request, 'carrinho/product_detail.html',
                  {'product': product})
