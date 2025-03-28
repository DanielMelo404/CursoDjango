from django.forms import ModelForm
from .models import Discusion

class FormularioDiscusion(ModelForm):
    class Meta():
        model = Discusion
        fields = '__all__' 