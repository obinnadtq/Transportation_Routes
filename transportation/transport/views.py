from django.shortcuts import render
from .models import Line, Stop, Station
from .forms import LineForm, StationForm, StopForm
from django.views.generic import TemplateView, ListView,CreateView, DeleteView, UpdateView
# Create your views here.
class HomeView(TemplateView):
    template_name = "transport/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["lines"] = Line.objects.all()
        context["stations"] = Station.objects.all()
        context["stops"] = Stop.objects.all()
        return context


class LinesView(ListView):
    template_name = "transport/lines.html"
    model= Line

class CreateLineView(CreateView):
    template_name = "transport/add_line.html"
    form_class = LineForm
    model = Line

class DeleteLineView(DeleteView):
    template_name = "transport/delete_line.html"
    success_url = "/lines/"
    model = Line

class UpdateLineView(UpdateView):
    template_name = "transport/update_line.html"
    model = Line
    form_class = LineForm

class StationsView(ListView):
    template_name = "transport/stations.html"
    model = Station

class CreateStationView(CreateView):
    template_name = "transport/add_station.html"
    form_class = StationForm
    model = Station

class DeleteStationView(DeleteView):
    template_name = "transport/delete_station.html"
    model = Station
    success_url = "/stations/"

class UpdateStationView(UpdateView):
    template_name = "transport/update_station.html"
    model = Station
    form_class = StationForm

class StopsView(ListView):
    template_name = "transport/stops.html"
    model= Stop


class CreateStopView(CreateView):
    template_name = "transport/add_stop.html"
    form_class = StopForm
    model = Stop

class DeleteStopView(DeleteView):
    template_name = "transport/delete_stop.html"
    model = Stop
    success_url = "/stops/"


class UpdateStopView(UpdateView):
    template_name = "transport/update_stop.html"
    model = Stop
    form_class = StopForm
