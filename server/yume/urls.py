from django.urls import path
from .views import OrderListView, OrderDetailView, OrderProductDetailView, ProductListView, ProductDetailView, StatisticView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:order_pk>/products/<int:order_product_pk>/',
         OrderProductDetailView.as_view(), name='order-product-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('statistics/', StatisticView.as_view(), name='order-statistic')
]
