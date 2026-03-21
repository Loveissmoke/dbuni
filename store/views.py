from django.shortcuts import render, get_object_or_404
from .models import Brand, Product

def home(request):
    brands = Brand.objects.all()
    return render(request, 'home.html', {'brands': brands})


def brand_detail(request, id):
    brand = get_object_or_404(Brand, id=id)
    products = Product.objects.filter(brand=brand)
    return render(request, 'brand_detail.html', {
        'brand': brand,
        'products': products
    })
