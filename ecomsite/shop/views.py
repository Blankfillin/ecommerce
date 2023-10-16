from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products


# Create your views here.
def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get("item_name")
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 4)
    page = request.GET.get("page")
    product_objects = paginator.get_page(page)

    return render(request, "shop/index.html", {"product_objects": product_objects})


def product_detail(request, pk):
    product = Products.objects.get(pk=pk)

    return render(request, "shop/detail.html", {"product_object": product})
