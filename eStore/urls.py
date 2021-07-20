from django.urls import path
from .views import ProductsList, ProductDetail

urlpatterns = [
    path('', ProductsList.as_view(), name='products-list'),
    path('<str:slug>/', ProductDetail.as_view(), name='product-detail'),

]
