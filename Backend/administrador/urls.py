from django.urls import path, include
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from . import views
app_name = "administrador"

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('menu/', views.menu, name='menu'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/modificar/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('accounts/', include('django.contrib.auth.urls')),  # Agrega esta línea para manejar las rutas de autenticación
]