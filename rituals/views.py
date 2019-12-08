from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from rituals.models import Ceremony
from rituals.forms import CeremonyForm

# Create your views here.

class CeremonyListView(ListView):
    """ Renders a list of all ceremonies. """
    model = Ceremony

    def get(self, request):
        """ GET a list of ceremonies. """
        ceremonies = self.get_queryset().all()
        return render(request, 'rituals/index.html', {
            'ceremonies': ceremonies
        })

class CeremonyDetailView(DetailView):
    """ Renders a specific ceremony based on it's slug. """
    model = Ceremony

    def get(self, request, slug):
        """ Returns a specific ceremony page by slug. """
        ceremony = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'ceremony.html', {
            'ceremony': ceremony
        })

class CeremonyCreateView(CreateView):
    """ Renders a form for creating a new ceremony. """
    def get(self, request, *args, **kwargs):
        context = {'form': CeremonyForm()}
        return render(request, 'new_ceremony.html', context)

    def post(self, request, *args, **kwargs):
        form = CeremonyForm(request.POST)
        if form.is_valid():
            ceremony = form.save()
            return HttpResponseRedirect(reverse_lazy('ceremony-details-page', args=[ceremony.slug]))
        return render(request, 'new_ceremony.html', {'form':form})
