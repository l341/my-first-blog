# Logica de la aplicacion

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

# Se define una funcion
# render -> reproduce la plantilla
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail (request, pk):
    # Si no existe el archivo te lleva a la pagina de error
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})