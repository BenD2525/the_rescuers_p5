from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from .models import Product
from django.db.models import Q


def products_list(request):
    ''' Returns the products page.'''
    serialized_products = []
    products = Product.objects.all()
    query = None

    for product in products:
        serialized_products.append({
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "image_url": product.image_url,
            "id": product.id,
        })  

    if 'search' in request.GET:
        query = request.GET['search']
        if not query:
            messages.error(request, "Please enter search criteria")
            return redirect(reverse('products:products_list'))
        
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        serialized_products = products.filter(queries)

    context = {
        "products": serialized_products,
        "search": query, 
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


