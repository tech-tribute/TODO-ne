from django import forms
from .models import Todo

class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title",)

class EditTodoForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
