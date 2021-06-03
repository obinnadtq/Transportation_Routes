from django.shortcuts import render
from .models import Line
from .forms import LineForm
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name = "transport/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["lines"] = Line.objects.all()
        return context