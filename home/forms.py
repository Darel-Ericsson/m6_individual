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
        # extra_fields = ['field']

    def __init__(self, *args, **kwargs): #añadir clases a los campos del form
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
