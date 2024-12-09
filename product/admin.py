from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "price",
        "quantity",
    )

    list_display_links = (
        "id",
        "name",
        "price",
        "quantity",
    )

    