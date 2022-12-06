from django.shortcuts import redirect, render
from .models import Product


def products_list(request):
    ''' Returns the products page.'''
    serialized_products = []
    products = Product.objects.all()

    for product in products:
        serialized_products.append({
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "image_url": product.image_url,
            "id": product.id,
        })     
    context = {
        "products": serialized_products
        }

    return render(request, 'products/products_list.html', context)


def product_detail(request, item_id):
    ''' Returns the product detail page.'''
    product = Product.objects.get(id=item_id)
    context = {
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "image": product.image,
        "id": product.id,
        "image_url": product.image_url,
        }

    return render(request, 'products/product_detail.html', context)


