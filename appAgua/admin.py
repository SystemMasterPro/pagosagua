from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TesoreroResource(resources.ModelResource):
    class Meta:
        model = Tesorero

class TesoreroAdmin(ImportExportModelAdmin):
    list_display = ('nombres','apellidos','cedula','celular','correo','estado')
    search_fields = ['cedula','nombres','apellidos']
    resource_class = TesoreroResource

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(ImportExportModelAdmin):
    list_display = ('usuarioAgua','nombres','apellidos','cedula','celular','correo')
    search_fields = ['cedula','nombres','apellidos']
    resource_class = UsuarioResource

class PagoResource(resources.ModelResource):
    class Meta:
        model = Pago

class PagoAdmin(ImportExportModelAdmin):
    list_display = ('usuario','tesorero','mesDesde','mesHasta','costoServicio')
    search_fields = ['mesDesde']
    resource_class = PagoResource

class ServicioAguaResource(resources.ModelResource):
    class Meta:
        model = ServicioAgua

class ServicioAguaAdmin(ImportExportModelAdmin):
    list_display = ('usuario','costoActivacion','motivoSuspension','estado')
    resource_class = ServicioAguaResource

admin.site.register(Tesorero, TesoreroAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(ServicioAgua, ServicioAguaAdmin)
