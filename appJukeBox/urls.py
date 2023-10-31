from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_estilos, name='index'),
    path('estilos/<int:estilo_id>/', views.show_estilo, name='estilo'),
    path('bandas', views.index_bandas, name='bandas'),
    path('bandas/<int:banda_id>', views.show_banda, name='banda'),
    path('paises', views.index_paises, name='paises'),
    path('paises/<int:pais_id>', views.show_pais, name='pais'),
]