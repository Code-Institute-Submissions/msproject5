from django.shortcuts import render
from products.models import Product
# Create your views here.


def do_search(request):
    """Search on product page"""
    products = Product.objects.filter(product_name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
