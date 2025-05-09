from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # Ensure the correct URL name
    path('product/create/', views.product_create, name='product_create'),
    path('product/update/<int:pk>/', views.product_edit, name='product_update'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('register/', views.register, name='register')
]
