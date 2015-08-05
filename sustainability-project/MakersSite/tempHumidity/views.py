#tempHumidity views
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import datetime

# Create your views here.
from .models import tempHumidity

class IndexView(generic.ListView):
    template_name = 'tempHumidity/index.html'
    context_object_name = 'Latest_Temps_List'
    def get_queryset(self):
        """Return the last five published questions."""
        return tempHumidity.objects.filter(
        date_rec__lte=timezone.now()
        ).order_by('-date_rec')[:5]


class DetailView(generic.DetailView):
    model = tempHumidity
    template_name = 'tempHumidity/detail.html'

def index(request):
    Latest_Temps_List = UserName.objects.order_by('-last_name')[:50]
    context = {'Latest_Temps_List': Latest_Temps_List}
    return render( request, 'tempHumidity/index.html', context)

@require_POST
def submit(request):
    tempHumidity( pi_num = request.POST['pi_num'], temperature = request.POST['temperature'], humidity = request.POST['humidity'], date_rec = datetime.datetime.fromtimestamp(int(request.POST['date_rec']) ) ).save()
    return HttpResponse('ok')
