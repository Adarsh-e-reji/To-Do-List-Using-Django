#This file defines the form used for reordering tasks.
from django import forms

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()