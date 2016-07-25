from django.shortcuts import render
from django.views import generic

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.utils import timezone

from .models import Location
from .forms import PostForm

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

def location_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            print(dir(request))
            #location.location = request.location
            location.pub_date = timezone.now()
            location.save()
            #return redirect('views', pk=location.pk)
            return HttpResponseRedirect(reverse('gmaps:index'))
    else:
        form = PostForm()
    return render(request, 'gmaps/location_edit.html', {'form': form})
"""
class ResultsView(generic.DetailView):
    model = Location 
    template_name = 'polls/results.html'

"""
