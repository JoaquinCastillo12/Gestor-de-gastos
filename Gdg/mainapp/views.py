from django.shortcuts import render
from .models import Gasto, Categoria, Usuario, Ingreso
from django.shortcuts import render, redirect
from django.http import HttpResponse


def login_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        contraseña = request.POST.get("contraseña")

        try:
            usuario = Usuario.objects.get(nombre=nombre)
            if usuario.contraseña == contraseña: 
                request.session["usuario_id"] = usuario.id  
                return redirect("dashboard")  
            else:
                return HttpResponse("Contraseña incorrecta")
        except Usuario.DoesNotExist:
            return HttpResponse("Usuario no encontrado")

    return render(request, "login.html")

def logout_view(request):
    request.session.flush()
    return redirect("login")


def dashboard_view(request):
    usuario_id = request.session.get("usuario_id")
    if not usuario_id:
        return redirect("login")  # Si no hay usuario, redirige a login

    # Obtener gastos e ingresos del usuario logueado
    gastos = Gasto.objects.filter(usuario_id=usuario_id)
    ingresos = Ingreso.objects.filter(usuario_id=usuario_id)

    # Calcular saldo total, total de gastos y total de ingresos
    total_gastos = sum(g.monto for g in gastos)
    total_ingresos = sum(i.monto for i in ingresos)
    saldo_actual = total_ingresos - total_gastos

    # Pasar los datos al template
    context = {
        "gastos": gastos[:5],  # Mostrar solo los últimos 5 gastos
        "ingresos": ingresos[:5],  # Mostrar solo los últimos 5 ingresos
        "total_gastos": total_gastos,
        "total_ingresos": total_ingresos,
        "saldo_actual": saldo_actual,
    }
    return render(request, "lista_gastos.html", context)
        

def gastos_view(request):
    usuario_id = request.session.get("usuario_id")  
    if not usuario_id:
        return redirect("login") 
    gastos = Gasto.objects.filter(usuario_id=usuario_id)  
    return render(request, "gastos.html", {"gastos": gastos})

def ingresos_view(request):
    usuario_id = request.session.get("usuario_id")  
    if not usuario_id:
        return redirect("login") 
    ingresos = Ingreso.objects.filter(usuario_id=usuario_id)  
    return render(request, "ingresos.html", {"ingresos": ingresos})