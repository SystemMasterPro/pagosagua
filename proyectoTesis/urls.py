"""proyectoTesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appAgua.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='vista_login'),
    path('inicio/', inicio_view, name='vista_inicio'),
    path('logout/', logout_view, name='vista_logout'),

    path('crearUsuario/', registrarUsuario_view, name='crearUsuario'),
    path('listar_usuario/',login_required(ListadoUsuarios.as_view()), name='listar_usuario'),
    path('modificarUsuario/<int:pk>/',login_required(ActualizarUsuario.as_view()), name='vista_modificarUsuario'),
    
    path('crearTesorero/', login_required(CrearTesorero.as_view()), name='vista_crearTesorero'),
    path('listarTesoreros/',login_required(ListadoTesoreros.as_view()), name='listar_tesoreros'),
    path('editarTesorero/<int:pk>/',login_required(ActualizarTesorero.as_view()), name='vista_editarTesorero'),
    
    path('listarServicios/',login_required(ListadoServicios.as_view()), name='vista_listarServicios'),
    path('nuevoServicio/',login_required(NuevoServicioAgua.as_view()), name='vista_nuevoServicioAgua'),
    path('activarServicio/<int:pk>/',login_required(ActivarServicio.as_view()), name='vista_activarServicio'),
    path('suspenderServicio/<int:pk>/',login_required(SuspenderServicio.as_view()), name='vista_suspenderServicio'),

    path('listarPagos/',login_required(ListadoPagos.as_view()), name='vista_listarPagos'),
    path('crearPago/',login_required(CrearPago.as_view()), name='vista_crearPago'),
    path('modificarPago/<int:pk>/',login_required(ActualizarPago.as_view()), name='vista_modificarPago'),

    path('consultar/<int:pk>/',login_required(ConsultaPagos.as_view()), name='vista_consultarInformacion'),
    path('recibo/<int:pk>/', login_required(ReciboPdf.as_view()), name="recibo")

]

admin.site.site_header = 'SISTEMA DE PAGOS DE AGUA'