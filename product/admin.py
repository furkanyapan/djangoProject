from django.contrib import admin

from product.models import Category, Product, Images


# Register your models here.

class ProductImageInLine(admin.TabularInline):
    model = Images
    extra = 5
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'status']
    list_filter = ['status', 'category']
    inlines = [ProductImageInLine]

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'product','image']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImageAdmin)
