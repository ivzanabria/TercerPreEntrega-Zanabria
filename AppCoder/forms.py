from django import forms


class CursoFormulario(forms.Form):
    # Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)


class EstudiantesForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class EntregableForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField(required=False)


class BuscarForms(forms.Form):
    nombre = forms.CharField(max_length=30)
