from django.contrib import admin
from myApp.models import Product, Category
from myApp import models

# Register your models here.


# myModel = [Product, Category]
# @admin.register(Product)
# @admin.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name','price','description', 'category')
    list_display = ('name', 'price','description', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


