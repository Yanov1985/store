from django.contrib import admin

# Register your models here.
from demo.models import *


admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
    search_fields = ('name',)
    ordering = ('name', 'price', 'quantity', )


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0