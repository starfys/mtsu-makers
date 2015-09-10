from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import datetime

from .models import project
# Create your views here.
class IndexView(generic.ListView):
    template_name ='ongoingProject/index.html'
    context_object_name ='Latest_Projects_List'

    def get_queryset(self):
        return project.filter(start_date__lte=timezone.now()).order_by('-start_date')[:10]
def matrix(request):
    return render(request, 'ongoingProjects/formtest.html')
