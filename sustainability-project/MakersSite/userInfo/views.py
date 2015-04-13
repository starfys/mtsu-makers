from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.utils import timezone
from .models import UserName

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'userInfo/index.html'
	context_object_name = 'User_Name_List'

	def get_queryset(self):
		"""Return the last fifty published userNames."""
		return UserName.objects.order_by('-last_name')[:50]
		#return UserName.objects.all()
		
class DetailView(generic.DetailView):
	model = UserName
	template_name = 'userInfo/detail.html'
	
def detail(request, userName_id):
	return HttpResponse("You're looking at User Name %s." % userName_id)

def results(request, userName_id):
	userName = get_object_or_404(userName, pk=userName_id)
	return render(request, 'userInfo/results.html', {'UserName': UserName})
	

def index(request):
	User_Name_List = UserName.objects.order_by('-last_name')[:50]
	context = {'User_Name_List': User_Name_List}
	return render(request, 'userInfo/index.html', context)
	
