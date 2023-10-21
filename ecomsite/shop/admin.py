from django.contrib import admin
from .models import Products, Order

# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "E-commerce Title"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = "Default category"
    list_display = (
        "title",
        "price",
        "discount_price",
        "category",
    )
    fields = (
        "title",
        "price",
    )
    search_fields = ("title", "category")
    actions = (change_category_to_default,)
    list_editable = ("price", "category")


admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
