from django.urls import path
from . import views  # Importamos las vistas creadas

urlpatterns = [
    # Detalles
    # CRUD Categorías
    path("categorias/", views.lista_categorias, name="lista_categorias"),
    path("categorias/crear/", views.crear_categoria, name="crear_categoria"),
    path("categorias/<int:pk>/actualizar/", views.actualizar_categoria, name="actualizar_categoria"),
    path("categorias/<int:pk>/eliminar/", views.eliminar_categoria, name="eliminar_categoria"),
    path("categorias/<int:pk>/", views.detalle_categoria, name="detalle_categoria"),

    # CRUD Productos
    path("productos/", views.lista_productos, name="lista_productos"),
    path("productos/crear/", views.crear_producto, name="crear_producto"),
    path("productos/<int:pk>/actualizar/", views.actualizar_producto, name="actualizar_producto"),
    path("productos/<int:pk>/eliminar/", views.eliminar_producto, name="eliminar_producto"),
     path("productos/<int:pk>/", views.detalle_producto, name="detalle_producto"),

    # CRUD Marcas
    path("marcas/", views.lista_marcas, name="lista_marcas"),
    path("marcas/crear/", views.crear_marca, name="crear_marca"),
    path("marcas/<int:pk>/actualizar/", views.actualizar_marca, name="actualizar_marca"),
    path("marcas/<int:pk>/eliminar/", views.eliminar_marca, name="eliminar_marca"),
    path("marcas/<int:pk>/", views.detalle_marca, name="detalle_marca"),
]
