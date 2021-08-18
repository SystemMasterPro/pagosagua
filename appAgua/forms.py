from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username','password']

class UsuarioForm(UserCreationForm):
    nombres = forms.CharField(widget=forms.TextInput())
    apellidos = forms.CharField(widget=forms.TextInput())
    cedula = forms.CharField(widget= forms.TextInput())
    celular = forms.CharField(widget= forms.TextInput())
    correo = forms.EmailField(widget= forms.EmailInput())

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['usuario','tesorero','mesDesde','mesHasta','costoServicio']
        labels = {
            'usuario': 'Usuario',
            'tesorero': 'Tesorero',
            'mesDesde': 'Mes desde',
            'mesHasta': 'Mes hasta',
            'costoServicio': 'Costo Servicio',
        }
        widgets = {
            'usuario':forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'',
                    'id':'usuario'
                }
            ),
            'tesorero':forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'',
                    'id':'tesorero'
                }
            ),
            'mesDesde':forms.DateInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'AAAA-mm-dd',
                    'id':'mesDesde'
                }
            ),
            'mesHasta':forms.DateInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'AAAA-mm-dd',
                    'id':'mesHasta'
                }
            ),
            'costoServicio':forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'0.0',
                    'id':'costoServicio'
                }
            ),
        }

class UsuarioForms(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['usuarioAgua','nombres','apellidos','cedula','celular','correo']
        labels = {
            'usuarioAgua': 'Usuario',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cedula': 'N° Cedula',
            'celular': 'Celular',
            'correo': 'Correo',
        }
        widgets = {
            'usuarioAgua':forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'',
                    'id':'usuarioAgua'
                }
            ),
            'nombres':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los nombres',
                    'id':'nombres'
                }
            ),
            'apellidos':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos',
                    'id':'apellidos'
                }
            ),
            'cedula':forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su N° cedula',
                    'id':'cedula'
                }
            ),
            'celular':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su N° celular',
                    'id':'celular'
                }
            ),
            'correo':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su correo electrónico',
                    'id':'correo'
                }
            ),
        }

class TesoreroForm(forms.ModelForm):

    class Meta:
        model = Tesorero
        fields = ['nombres','apellidos','cedula','celular','correo']
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cedula': 'N° Cedula',
            'celular': 'Celular',
            'correo': 'Correo',
        }
        widgets = {
            'nombres':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los nombres',
                    'id':'nombres'
                }
            ),
            'apellidos':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos',
                    'id':'apellidos'
                }
            ),
            'cedula':forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su N° cedula',
                    'id':'cedula'
                }
            ),
            'celular':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su N° celular',
                    'id':'celular'
                }
            ),
            'correo':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su correo electrónico',
                    'id':'correo'
                }
            ),
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = ServicioAgua
        fields = ['usuario','costoActivacion','motivoSuspension']
        labels = {
            'usuario': 'Usuario',
            'costoActivacion': 'Costo de Activación',
            'motivoSuspension': 'Motivo de Suspensión',
            'estado': 'Estado',
        }
        widgets = {
            'usuario':forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'',
                    'id':'usuario'
                }
            ),
            'costoActivacion':forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'0.0',
                    'id':'costoActivacion'
                }
            ),
            'motivoSuspension':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el motivo de suspensión del servicio',
                    'id':'motivoSuspension'
                }
            ),
        }