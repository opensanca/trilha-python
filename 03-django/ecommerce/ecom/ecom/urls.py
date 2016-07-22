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
from carrinho.views import (login_view, logout_view, PersonCreateView,
                            ProductDetailView, ProductListView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ProductListView.as_view(), name='home'),
    url(r'^products/(?P<pk>\d+)$', ProductDetailView.as_view(),
        name='product_detail'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^signup/$', PersonCreateView.as_view(), name='person_create'),
]
