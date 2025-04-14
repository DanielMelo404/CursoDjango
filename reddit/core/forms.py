from django.forms import ModelForm
from .models import Discusion

class FormularioDiscusion(ModelForm):
    class Meta:
        model = Discusion
        fields = '__all__' 
        exclude = ['user']


# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         fields = ['username','email','password1','password2']