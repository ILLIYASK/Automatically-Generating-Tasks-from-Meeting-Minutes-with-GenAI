
from django import forms
from .models import MoM

class UploadMoM(forms.ModelForm):
    class Meta:
        model = MoM
        fields = ('title', 'pdf',)