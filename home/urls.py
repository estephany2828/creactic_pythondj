
from django.urls import path
from .views import *
from django.contrib.auth.models import User

urlpatterns = [
   path('quienes_somos/', quienes_somos_view, name= 'quienes_somos'),
    path('contactenos/', contactenos_view),
    path('nuestros_servicios/', nuestros_servicios_view),
    path('inicio/', inicio_view),
    path('lista_producto/', lista_producto_view, name="lista_productos"),
    path('agregar_producto/', agregar_producto_view, name='agregar_producto'),
    path('ver_producto/<int:id_producto>/', ver_producto_view, name="ver_producto"),
    path('editar_producto/<int:id_producto>/', editar_producto_view, name="editar_producto"),
    path('eliminar_producto/<int:id_producto>/', eliminar_producto_view, name="eliminar_producto"),
    path('desactivar_producto/<int:id_producto>/', desactivar_producto_view, name="desactivar_producto"),
    path('login/', login_view,name='login'),
    path('logout/', logout_view,name='logout'),
    path('register/',  register_view, name="vista_register"), 
    path('thanks_for_register/', thanks_for_register_view, name = 'thanks_for_register'),

]