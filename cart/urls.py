from django.urls import path
from .views import CartView, AddToCart


urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/add/", AddToCart.as_view(), name="add-to-cart"),
]