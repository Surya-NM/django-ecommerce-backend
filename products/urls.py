from django.urls import path
from .views import Clistcreateview, Cretriveupdatedestory, Plistcreateview, Pretriveupdatedestory

urlpatterns = [
    path('category/', Clistcreateview.as_view()),
    path('category/<int:pk>/', Cretriveupdatedestory.as_view()),

    path('products/', Plistcreateview.as_view()),
    path('products/<int:pk>/', Pretriveupdatedestory.as_view()),
]