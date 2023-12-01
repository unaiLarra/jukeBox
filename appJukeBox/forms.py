from django.forms import ModelForm
from .models import Banda, Estilo, Pais

class BandaForm(ModelForm):
    class Meta:
        model = Banda
        fields = "__all__"

class EstiloForm(ModelForm):
    class Meta:
        model = Estilo
        fields = "__all__"

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = "__all__"