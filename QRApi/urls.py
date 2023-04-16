from django.urls import path, include
from .views import QR

urlpatterns = [
    path('generate_qr/', QR.as_view()),
]
