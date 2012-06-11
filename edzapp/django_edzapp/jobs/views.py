from django.shortcuts import render_to_response
from django.template import RequestContext

from jobs.models import Job

def index(request):
	jobs = Job.objects.all()
	return render_to_response('index.html',
							  {"jobs" : jobs},
                              context_instance=RequestContext(request))

def all(request):
	return render_to_response('jobs/all.html',
                              context_instance=RequestContext(request))

def saved(request):
	return render_to_response('jobs/saved.html',
                              context_instance=RequestContext(request))

def detail(request, job_id):
	return render_to_response('jobs/detail.html',
                              context_instance=RequestContext(request))
