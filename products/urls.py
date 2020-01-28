from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:product_id>/', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('services/', views.services, name='services'),
    path('service/<int:service_id>/', views.service, name='service'),
    path('productcomment/', views.productcomment, name='productcomment'),
]
