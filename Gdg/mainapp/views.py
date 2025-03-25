from django.shortcuts import render
from .models import Gasto, Categoria, Usuario


def gastos_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    gastos = Gasto.objects.filter(usuario=usuario)
    
    return render(request, 'lista_gastos.html', {
        'usuario': usuario,
        'gastos': gastos
    })

