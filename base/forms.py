from datetime import date
from base.models import Reparo, Roupa
from django import forms


class RegistrarReparoForm(forms.Form):
    reparo = forms.ModelChoiceField(Reparo.objects, label='Reparo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reparo'].queryset = Reparo.objects.filter(data_entrega__isnull=True)

    def processar(self):
        reparo = self.cleaned_data['reparo']
        reparo.data_entrega = date.today()
        reparo.restaurado = True
        reparo.save()