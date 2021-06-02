from django import forms
from .models import Todo


class TaskForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('task', 'overview', 'author', 'employee', 'status')
