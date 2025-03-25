from django.shortcuts import render
from .models import Gasto, Categoria, Usuario, Ingreso


def home(request):
    return render(request, 'lista_gastos.html', )
        

def gastos_view(request):
    gastos = Gasto.objects.all()
    return render(request, "gastos.html", {"gastos": gastos})

def ingresos_view(request):
    ingresos = Ingreso.objects.all()
    return render(request, "ingresos.html", {"ingresos": ingresos})