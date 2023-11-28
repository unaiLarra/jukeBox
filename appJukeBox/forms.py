from django.forms import ModelForm
from .models import Banda

class BandaForm(ModelForm):
    class Meta:
        model = Banda
        fields = ('nombre','pais','descripcion','estilos','imagen')