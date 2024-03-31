from django.urls import path
from.views import home,cart,profile,payment,product_list

urlpatterns = [
    path('',home),
    path('product_list/',product_list),
    path('cart/',cart),
    path('profile/',profile),
    path('payment/',payment),
]