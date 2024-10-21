from django.shortcuts import redirect
from functools import wraps
from .models import UserMilitar

def usuario_autenticado(view_func):
    @wraps(view_func)  # Preserva o nome da função original
    def wrapper(request, *args, **kwargs):
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("login")
        
        try:
            usuario = UserMilitar.objects.get(id=user_id)
            request.usuario = usuario
        except UserMilitar.DoesNotExist:
            return redirect("login")

        return view_func(request, *args, **kwargs)
    return wrapper
