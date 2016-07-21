"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from carrinho.views import (login_view, logout_view, person_create_view,
                            product_detail_view, product_list_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', product_list_view, name='home'),
    url(r'^products/(?P<key>\d+)$', product_detail_view,
        name='product_detail'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^signup/$', person_create_view, name='person_create'),
]
