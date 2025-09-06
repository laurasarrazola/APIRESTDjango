from django.urls import path
from . import views  # Importamos las vistas creadas

urlpatterns = [
    path("categorias/", views.lista_categorias, name="lista_categorias"),
    path("productos/", views.lista_productos, name="lista_productos"),
    path("marcas/", views.lista_marcas, name="lista_marcas"),
]
