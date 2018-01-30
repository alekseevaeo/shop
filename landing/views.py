from django.shortcuts import render, redirect
from django.contrib import auth
from products.models import ProductImage


def home(request):
    products_images = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True)
    products_images_cezve = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True,
                                                        product__product_category=1)
    products_images_milk_jugs = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True,
                                                            product__product_category=2)
    products_images_miski = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True,
                                                            product__product_category=3)
    products_images_dishes = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True,
                                                            product__product_category=4)
    products_images_cups = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True,
                                                            product__product_category=5)
    username = auth.get_user(request).username
    return render(request, 'landing/home.html', locals())