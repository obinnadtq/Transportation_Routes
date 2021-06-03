from django import forms
from .models import Line, Station, Stop



class LineForm(forms.ModelForm):
  class Meta:
    model = Line
    fields = "__all__"


class StationForm(forms.ModelForm):
  class Meta:
    model = Station
    fields = "__all__"


class StopForm(forms.ModelForm):
  class Meta:
    model = Stop
    fields = "__all__"

