# Importamos la funcion de Django path y las views
from django.urls import path
from . import views

# Estamos asociando una vista, post_list a la URL de raiz
# views.post_list -> lugar al que ir si se entra en el sitio web
# name='post_list' ->  nombre de la URL que se utilizara para identificar a la vista
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]