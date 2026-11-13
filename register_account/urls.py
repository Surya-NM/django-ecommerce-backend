from django.urls import path
from .views import Signup,LoginView,Logoutview

urlpatterns = [
    path('register/', Signup.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logoutview.as_view())
]