"""zeply URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main.views import btc_address, BTCAddressView, BTCAddressList, \
    ETHAddressView, ETHAddressList, eth_address

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-btc-address/', btc_address),
    path('btc-addresses/', BTCAddressList.as_view()),
    path('btcaddress/<int:pk>/', BTCAddressView.as_view()),
    path('create-eth-address/', eth_address),
    path('eth-addresses/', ETHAddressList.as_view()),
    path('eth-address/<int:pk>/', ETHAddressView.as_view()),
]
