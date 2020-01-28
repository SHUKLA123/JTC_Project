from django.contrib import admin

from .models import Contact, ServiceContact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'email', 'order', 'completed', 'product', 'contact_date') #
    list_display_links = ('name', 'id')
    search_fields = ('name', 'email', 'order', 'product') #
    list_editable = ('completed',)
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)

class ServiceContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'email', 'order', 'completed', 'service', 'contact_date') #
    list_display_links = ('name', 'id')
    search_fields = ('name', 'email', 'order', 'service')
    list_editable = ('completed',)

    list_per_page = 25

admin.site.register(ServiceContact, ServiceContactAdmin)
