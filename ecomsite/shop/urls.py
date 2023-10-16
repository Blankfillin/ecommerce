from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
    path("products/<int:pk>", views.product_detail, name="product_detail"),
]
