#makerSite views
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


#http://grasshopperpebbles.com/django-python/how-to-set-up-a-home-page-with-django/
def index (request):
  return render_to_response('MakersSite/index.html', context_instance=RequestContext(request))

def street (request):
  return render_to_response('MakersSite/street.html', context_instance=RequestContext(request))
