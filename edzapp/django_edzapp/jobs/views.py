from django.shortcuts import render_to_response
from django.template import RequestContext

from jobs.models import Job

def index(request):
	jobs = Job.objects.all()
	return render_to_response('index.html',
							  {"jobs" : jobs},
                              context_instance=RequestContext(request))
