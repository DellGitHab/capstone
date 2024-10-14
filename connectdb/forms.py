from django import forms
from .models import Personnel

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['first_name', 'last_name', 'email', 'address', 'contact_number', 'rfid_tag']
