from django.contrib import admin
from .models import Product, Review
# Register your models here.
admin.site.register(Product)
admin.site.register(Review)

class ReviewAdmin (admin.ModelAdmin):
    list_display = ('product', 'user', 'rating',  'created_at')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)