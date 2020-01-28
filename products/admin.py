from django.contrib import admin

from .models import Product, ProductComment, Service

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'local_name', 'is_published', 'price', 'list_date', 'customisable', 'is_trending')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'local_name', 'is_published', 'customisable')
    list_editable = ('is_published', 'customisable', 'is_trending')
    search_fields = ('name', 'local_name', 'description', 'price', 'is_trending')
    list_per_page = 25

admin.site.register(Product, ProductAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('name', 'price')
    list_per_page = 25

admin.site.register(Service, ServiceAdmin)


class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'comment', 'rating', 'is_published', 'list_date')
    list_display_links = ('id', 'name', 'product')
    list_filter = ('name', 'product', 'is_published', 'rating')
    list_editable = ('is_published',)
    search_fields = ('name', 'product', 'rating')
    list_per_page = 25

admin.site.register(ProductComment, ProductCommentAdmin)
