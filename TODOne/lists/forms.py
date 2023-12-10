from django import forms


class CreateListForm(forms.Form):
    name = forms.CharField(max_length=255, label="", required=True,)
