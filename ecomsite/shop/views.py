from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products, Order


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


def checkout(request):
    if request.method == "POST":
        items = request.POST.get("items", "")
        total = request.POST.get("total", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        state = request.POST.get("staet", "")
        zipcode = request.POST.get("zipcode", "")

        order = Order(
            items=items,
            total=total,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
        )

        order.save()

    return render(request, "shop/checkout.html")
