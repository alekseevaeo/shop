from django.shortcuts import render
from products.models import *
from django.contrib import auth

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    username = auth.get_user(request).username
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(session_key)

    return render(request, 'products/product.html', locals())


def products(request, product_category_id):
    products = ProductCategory.objects.get(id=product_category_id)
    username = auth.get_user(request).username
    return render(request, 'products/show_products.html', locals())
