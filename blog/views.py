# Logica de la aplicacion

from django.shortcuts import render

# Create your views here.

# Se define una funcion
# render -> reproduce la plantilla
def post_list(request):
    return render(request, 'blog/post_list.html', {})