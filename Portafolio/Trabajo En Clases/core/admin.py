from django.contrib import admin

# Register your models here.
from .models import Category, SubCategory, Brand, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "category_name",
        "user",
        "timestamp",
        "status"
    ]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "subcategory_name",
        "category",
        "user",
        "timestamp",
        "status"
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        "brand_name",
        "user",
        "timestamp",
        "status"
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "product_name",
        "user",
        "timestamp",
        "status"
    ]