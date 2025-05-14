from django import forms
from .models import Veiculo

class VeiculoForm(forms.ModelForm):
    class Meta:
        widgets={
            'marca' : forms.Select(attrs={"class":"form-control "}),
            'ano':forms.NumberInput(attrs={"class":"form-control "}),
            'combustivel': forms.Select(attrs={"class":"form-control "}),
            "modelo":  forms.TextInput(attrs={"class":"form-control "}),
            'cor': forms.Select(attrs={"class":"form-control"}),
        }
        model = Veiculo
        fields = ['modelo','ano','combustivel','marca','cor','foto']
