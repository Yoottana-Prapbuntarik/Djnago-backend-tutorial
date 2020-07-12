from django.contrib import admin
from .models import Orderuser, Productinorder
# Register your models here.


class OrderuserAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'author', 'first_name',
                    'last_name', 'total_cost', 'telephone_number']


class ProductinorderAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_cost', 'quantity', 'order', ]


admin.site.register(Orderuser, OrderuserAdmin)
admin.site.register(Productinorder, ProductinorderAdmin)
