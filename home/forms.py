from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','rut','first_name','last_name','email','phone','birthday']
        labels = {'Usuario':'username',
                  'RUT':'rut',
                  'Nombre':'first_name',
                  'Apellido':'last_name',
                  'Email':'email',
                  'Teléfono':'phone',
                  'Nacimiento':'birthday'}
