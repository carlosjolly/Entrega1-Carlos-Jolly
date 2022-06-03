from django import forms

class trabajoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    trabajo = forms.CharField(max_length=40)

class contactoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)
    telefono = forms.IntegerField()