# api/urls.py (CORRECTED)
from django.urls import path
from .views import register, EmailTokenObtainPairView

urlpatterns = [
    path('register/', register),
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
