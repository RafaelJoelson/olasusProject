# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import AgenteDeSaude

class AgenteDeSaudeAuthenticationForm(AuthenticationForm):
    class Meta:
        model = AgenteDeSaude
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


