from django import forms
from .models import Escada

class EscadaForm(forms.ModelForm):
    class Meta:
        model = Escada
        fields = '__all__'
        widgets = {
    'problema': forms.Textarea(attrs={'placeholder': 'Descreva o problema'}),
    'data_envio': forms.DateInput(attrs={'type': 'date'})
}