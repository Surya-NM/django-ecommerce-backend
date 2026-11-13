
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('register_account.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', include('products.urls')),
    path("api/", include("cart.urls")),
    path("api/orders/", include("ordermanagement.urls")),
]
