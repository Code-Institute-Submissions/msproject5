"""msproject5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from pages.views import home_view, contact_view, register_view, products_view, login_view, cart_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('product/', products_view, name='products'),
    path('cart/', cart_view, name='cart'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('contact/', contact_view, name='contact'),
    path('logout/', logout_view, name='logout'),

    path('admin/', admin.site.urls),
]
