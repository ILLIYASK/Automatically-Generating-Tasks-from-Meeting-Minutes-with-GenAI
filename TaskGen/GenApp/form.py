
from django import forms
from .models import MoM,Task

class UploadMoM(forms.ModelForm):
    class Meta:
        model = MoM
        fields = ('title', 'pdf',)

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'position', 'task', 'task_description', 'deadline']