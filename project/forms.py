from django import forms
from project.models import *

class TaskForm(forms.ModelForm):

    class Meta:

        model = Task

        fields = "__all__"