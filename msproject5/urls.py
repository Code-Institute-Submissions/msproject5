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

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cart import urls as urls_cart
from search import urls as urls_search
from orders import urls as urls_orders
from products import urls as urls_products
from pages.views import home_view, contact_view, subscribe_view
from django.conf.urls import url, include
from users import views as user_views

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('products/', include(urls_products)),
    path('view_cart/', include(urls_cart)),
    path('search/', include(urls_search)),
    path('orders/', include(urls_orders)),
    path('register/', user_views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), 
    path('contact/', contact_view, name='contact'),
    path('subscribe/', subscribe_view, name='subscribe'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('admin/', admin.site.urls),
]
