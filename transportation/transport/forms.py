from django import forms
from .models import Line



class LineForm(forms.ModelForm):
  class Meta:
    model = Line
    fields = "__all__"

