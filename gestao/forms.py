from django import forms
from .models import Prato, Mesa, Pedido


class PratoForm(forms.ModelForm):
    class Meta:
        model = Prato
        fields = ['nome', 'descricao', 'preco', 'categoria']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco is not None and preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")
        return preco


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'capacidade']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'capacidade': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }

    def clean_capacidade(self):
        capacidade = self.cleaned_data.get('capacidade')
        if capacidade is not None and capacidade <= 0:
            raise forms.ValidationError("A capacidade tem de ser maior que zero.")
        return capacidade


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['mesa', 'pratos', 'estado']
        widgets = {
            'mesa': forms.Select(attrs={'class': 'form-select'}),
            'pratos': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }