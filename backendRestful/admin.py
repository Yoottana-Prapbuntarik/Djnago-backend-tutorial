from django.contrib import admin
from .models import Allproduct

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'product_cost', 'published','pub_date']
	search_fields = ('product_name', 'product_price')
	list_filter = ('published',)
	date_hierarchy = 'pub_date'
	    
admin.site.register(Allproduct, ProductAdmin)