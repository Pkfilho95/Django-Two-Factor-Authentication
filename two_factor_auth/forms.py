from django import forms

from .models import TwoFactorAuthModel

class TwoFactorAuthForm(forms.ModelForm):
    
    class Meta:
        model = TwoFactorAuthModel
        fields = ['token']