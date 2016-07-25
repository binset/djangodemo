from django.shortcuts import render
from django.views import generic

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from django.utils import timezone

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

def add_location(request, location):
    l = Location(location=location, pub_date=timezone.now())
    l.save()
    return HttpResponseRedirect(reverse('gmaps:index'))
    #return HttpResponse("You're looking at location %s." % location)

def delete_location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    location.delete()
    return HttpResponse("You're looking at deleting location %s." % location)

"""
class ResultsView(generic.DetailView):
    model = Location 
    template_name = 'polls/results.html'

"""
