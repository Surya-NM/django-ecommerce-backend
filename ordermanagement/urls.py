from django.urls import path

from .views import (
    CreateOrderAPIView,
    OrderListAPIView,
    OrderDetailAPIView,
    CancelOrderAPIView,
      AdminOrderList,
    AdminOrderStatusUpdateAPIView
)

urlpatterns = [
    path("create/", CreateOrderAPIView.as_view(), name="create-order"),
    path("", OrderListAPIView.as_view(), name="order-list"),
    path("<int:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),
    path("<int:pk>/cancel/", CancelOrderAPIView.as_view(), name="cancel-order"),
     path(
        "admin/orders/",
        AdminOrderList.as_view(),
        name="admin-order-list"
    ),

    path(
        "admin/orders/<int:pk>/status/",
        AdminOrderStatusUpdateAPIView.as_view(),
        name="admin-order-status"
    ),
]