from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm


# Este formulario se debe immportar en las Views y luego enviar al template 
class ContactoForms (forms.ModelForm):
    class Meta:
        model=Contacto
        # fields=["nombre","email","tipo_cosulta","mensaje","avisos"]
        fields='__all__'
        
class CustomUserCreationForm(UserCreationForm):
    pass
        
        