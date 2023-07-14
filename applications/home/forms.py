from django import forms
from .models import Subscriber

class subscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = {
            'email',
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                    'class': 'input-form',
                }
            )
        }