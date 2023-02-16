from django.shortcuts import render
from product.models import *
# Create your views here.
def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')

def product_view(request):
    if request.method == "GET":
        prod = Products.objects.all()

        context = {
            'products': prod
        }
        return render(request, 'products/products.html', context=context)
