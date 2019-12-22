from django.urls import path

from .views import (
    product_list_view,
    product_detail_view,
    product_edit_view,
    product_delete_view,
    product_create_view,
    product_create2_view,
    product_search_view
    )

app_name='products'    
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('<int:currId>/', product_detail_view, name='product-detail'),
    path('<int:currId>/edit/', product_edit_view, name='product-edit'),
    path('<int:currId>/delete/', product_delete_view, name='product-delete'),
    path('create/', product_create_view, name='product-create'),
    path('create2/', product_create2_view, name='product-create2'),
    path('search/', product_search_view, name='product-search'),
]