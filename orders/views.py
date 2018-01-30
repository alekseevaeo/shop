from django.http import JsonResponse
from .models import ProductInBasket
from django.shortcuts import render


#  обновление корзины на всех страницах магазина
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    numb = data.get("nmb")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        product = ProductInBasket.objects.get(id=product_id)
        product.is_active=False
        product.save(force_update=True)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, is_active=True,
                                                                 defaults={"number": numb})
        if not created:
            new_product.number += int(numb)
            new_product.save(force_update=True)

    #common code for 2 cases
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_numb = products_in_basket.count()
    return_dict["product_total_numb"] = products_total_numb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["numb"] = item.number
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_numb = products_in_basket.count()
    return render(request, 'orders/checkout.html', locals())