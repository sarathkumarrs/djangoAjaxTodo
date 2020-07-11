from django import forms
from kseb.models import Task


class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = ('title',)   

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'})
        } 