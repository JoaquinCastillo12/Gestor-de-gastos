from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastos_usuario, name='gastos_usuario'),
]