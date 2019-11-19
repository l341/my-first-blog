# Logica de la aplicacion

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

# Se define una funcion
# render -> reproduce la plantilla
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})