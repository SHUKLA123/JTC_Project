from django.contrib import admin

from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'location', 'task')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'location', 'is_published', 'task')
    list_editable = ('is_published',)
    search_fields = ('name', 'location', 'is_published')
    list_per_page = 25


admin.site.register(Customer, CustomerAdmin)
