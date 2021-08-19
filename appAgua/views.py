from django.shortcuts import render, redirect
from io import BytesIO
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from xhtml2pdf import pisa
from django.template.loader import get_template

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/inicio/')
        form = LoginForm()
        ctx = {'form':form}
        return render(request,'login.html',ctx)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def inicio_view(request):
    usuario = Usuario.objects.all()
    ctx = {'usuario': usuario}
    return render(request,'vista_principal.html', ctx)

################     USUARIO     #################

class ListadoUsuarios(ListView):
    model = Usuario
    template_name = 'usuario/listar_usuarios.html'
    queryset = Usuario.objects.all()
    context_object_name = 'usuarios'

def registrarUsuario_view(request):
    info = "Usuario no creado"
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            usuario = Usuario()
            usuario.usuarioAgua = user
            usuario.nombres = form.cleaned_data['nombres']
            usuario.apellidos = form.cleaned_data['apellidos']
            usuario.cedula = form.cleaned_data['cedula']
            usuario.celular = form.cleaned_data['celular']
            usuario.correo = form.cleaned_data['correo']
            usuario.save()
            usuarios = Usuario.objects.all()
            ctx = {'usuarios':usuarios}
            return render(request,'usuario/listar_usuarios.html',ctx)
    else:
        form = UsuarioForm()
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
    ctx = {'form':form,'info':info}
    return render(request,'usuario/registrar_usuario.html',ctx)

class ActualizarUsuario(UpdateView):
    model = Usuario
    form_class = UsuarioForms
    template_name = 'usuario/modificar_usuario.html'
    success_url = reverse_lazy('listar_usuario')

class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'usuario/confirm_delete_usuario.html'
    def post(self, request, pk, *args, **kwargs):
        object = Usuario.objects.get(idUsuario=pk)
        object.delete()
        return HttpResponseRedirect('/listar_usuario/')

################     TESOREROS         ###############
class ListadoTesoreros(ListView):
    model = Tesorero
    template_name = 'tesorero/listar_tesoreros.html'
    queryset = Tesorero.objects.all()
    context_object_name = 'tesoreros'

class CrearTesorero(CreateView):
    model = Tesorero
    form_class = TesoreroForm
    template_name = 'tesorero/nuevo_tesorero.html'
    success_url = reverse_lazy('listarTesoreros')

class ActualizarTesorero(UpdateView):
    model = Tesorero
    form_class = TesoreroForm
    template_name = 'tesorero/modificar_tesorero.html'
    success_url = reverse_lazy('listarTesoreros')

################     PAGOS DE AGUA     ###############       

class ListadoPagos(ListView):
    model = Pago
    template_name = 'pagos/listar_pagos.html'
    queryset = Pago.objects.order_by('mesDesde')
    context_object_name = 'pagos'

class CrearPago(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pagos/nuevo_pago.html'
    success_url = reverse_lazy('vista_listarPagos')

class ActualizarPago(UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pagos/modificar_pago.html'
    success_url = reverse_lazy('vista_listarPagos')

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None

class ReciboPdf(View):
    def get(self, request, pk, *args, **kwargs):
        pago = Pago.objects.filter(idPago=pk)
        context = {'pago':pago}
        pdf = render_to_pdf('pagos/recibo-agua.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

#################       SERVICIOS DE AGUA        ################

class ListadoServicios(ListView):
    model = ServicioAgua
    template_name = 'servicios/listar_servicios.html'
    query_set = ServicioAgua.objects.all()
    context_object_name = 'servicios'

class NuevoServicioAgua(CreateView):
    model = ServicioAgua
    form_class = ServicioForm
    template_name = 'servicios/nuevo_servicioAgua.html'
    success_url = reverse_lazy('vista_listarServicios')

class SuspenderServicio(UpdateView):
    model = ServicioAgua
    form_class = ServicioForm
    template_name = 'servicios/suspender_servicio.html'
    def post(self, request, pk, *args, **kwargs):
        if request.method == 'POST':
            form = ServicioForm(request.POST)
            object = ServicioAgua.objects.get(idServicioAgua=pk)
            object.costoActivacion = form.data['costoActivacion']
            object.motivoSuspension = form.data['motivoSuspension']
            object.estado = False
            object.save()
            return HttpResponseRedirect('/listarServicios/')

class ActivarServicio(DeleteView):
    model = ServicioAgua
    template_name = 'servicios/activar_servicio.html'
    def post(self, request, pk, *args, **kwargs):
        object = ServicioAgua.objects.get(idServicioAgua=pk)
        object.costoActivacion = 0
        object.motivoSuspension = "Ningún motivo"
        object.estado = True
        object.save()
        return HttpResponseRedirect('/listarServicios/')

###############    CONSULTAR INFORMACION PAGOS DE AGUA     ################

class ConsultaPagos(ListView):
    def get(self, request, pk, *args, **kwargs):
        pagos = Pago.objects.filter(usuario=pk)
        context = {'pagos':pagos}
        return render(request, 'consultas/consultar_inf.html',context)
