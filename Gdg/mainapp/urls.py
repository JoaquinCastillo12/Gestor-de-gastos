from django.urls import path
from .views import gastos_view, ingresos_view, home

urlpatterns = [
    path("", home,name="home"),
    path("gastos/", gastos_view, name="gastos"),
    path("ingresos/", ingresos_view, name="ingresos"),
]
