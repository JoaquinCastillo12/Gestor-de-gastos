from django.urls import path
from .views import gastos_view, ingresos_view, dashboard_view, login_view, logout_view

urlpatterns = [
    path("", login_view,name="login"),
    path("logout/", logout_view, name="logout"), 
    path("dashboard/", dashboard_view, name="dashboard"),
    path("gastos/", gastos_view, name="gastos"),
    path("ingresos/", ingresos_view, name="ingresos"),
]
