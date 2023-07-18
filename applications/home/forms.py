from django import forms
from .models import Subscriber, Contact

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

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')


