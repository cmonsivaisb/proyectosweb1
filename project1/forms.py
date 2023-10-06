from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

    
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar la clase 'form-control' a todos los campos
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



# Otros formularios personalizados aquí
