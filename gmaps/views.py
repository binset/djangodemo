from django.shortcuts import render
from django.views import generic


from .models import Location

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'gmaps/index.html'
    context_object_name = 'latest_location_list'

    def get_queryset(self):
        """Return the last five locations."""
        return Location.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Location
    template_name = 'gmaps/detail.html'


"""
class ResultsView(generic.DetailView):
    model = Location 
    template_name = 'polls/results.html'

"""
