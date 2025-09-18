<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('subir/', views.subir_texto, name='subir_texto'),
    path('', views.lista_textos, name='lista_textos'),
    path('texto/<int:texto_id>/mle/', views.ngram_mle, name='ngram_mle'),
]
=======
from django.urls import path 
from . import views 

urlpatterns = [ 
    path('subir/', views.subir_texto, name='subir_texto'), 
    path('', views.lista_textos, name='lista_textos'), 
] 
>>>>>>> 76182a81822a6aa7a9c45c67f5f91222cbee9ddc
