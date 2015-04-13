from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.utils import timezone
# Create your views here.
from .models import tempHumidity

class IndexView(generic.ListView):
	template_name = 'tempHumidity/index.html'
	context_object_name = 'latest_temps'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-date_rec')[:5]

class DetailView(generic.DetailView):
	model = tempHumidity
	template_name = 'tempHumidity/detail.html'