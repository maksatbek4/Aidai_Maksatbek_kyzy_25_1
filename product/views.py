from django.shortcuts import render
from product.models import *
# Create your views here.
def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def product_view(request, products=None):
    if request.method == "GET":
        prod = Products.objects.all()

        context = {
            'products': [
                {
                    'id': products.id,
                    'title': products.title,
                    'image': products.image,
                    'hashtags': products.hashtags.all()
                } for products in products
            ]

        }
        return render(request, 'products/products.html', context=context)
def hashtags_view(request):
    if request.method == "GET":
        hashtags = Hashtag.objects.all()

        context = {
            'hashtags': hashtags
        }
        return render(request, 'products/hashtags.html', context=context)
