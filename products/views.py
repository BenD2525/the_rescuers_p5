from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from .models import Product
from django.db.models import Q
from django.db.models.functions import Lower


def products_list(request):
    ''' Returns the products page.'''
    serialized_products = []
    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    for product in products:
        serialized_products.append({
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "image_url": product.image_url,
            "id": product.id,
        })  

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            serialized_products = products.order_by(sortkey)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter search criteria")
                return redirect(reverse('products:products_list'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            serialized_products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        "products": serialized_products,
        "search": query,
        'current_sorting': current_sorting,
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


