from django.urls import path
from mpesa import views

urlpatterns = [
    path('', views.index, name='test'),
]
