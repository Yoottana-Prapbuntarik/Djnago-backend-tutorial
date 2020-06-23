from django.contrib import admin
from .models import Allproduct, UserAuth

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'product_cost', 'published','pub_date']
	search_fields = ('product_name', 'product_price')
	list_filter = ('published',)
	date_hierarchy = 'pub_date'
	    
		
class UserAdmin(admin.ModelAdmin):
		list_display = ['first_name', 'username', 'pub_date']
		list_display_links = ('first_name', 'username')
		list_filter = ('pub_date',)

admin.site.register(Allproduct, ProductAdmin)
admin.site.register(UserAuth, UserAdmin)