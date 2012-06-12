from django.shortcuts import render

from jobs.models import Job

def index(request):
    jobs = Job.objects.exclude(deadline=None).order_by("deadline")
    no_deadlines = Job.objects.exclude(date_posted=None).filter(deadline=None).order_by("date_posted")
    return render(request, 'jobs/index.html', {"jobs" : jobs, 
                                                "no_deadlines" : no_deadlines})

def all(request):
    return render(request, 'jobs/all.html')

def saved(request):
    return render(request, 'jobs/saved.html')

def detail(request, job_id):
    return render(request, 'jobs/detail.html')

def star(request, job_id):
    #TODO: fix csrf
    if request.method == "POST":
        job = Job.objects.get(job_id=job_id)
        request.user.job_set.add(job)
        return
    else:
        render(request, 'jobs/star.html')

def unstar(request, job_id):
    if request.method == "POST":
        job = Job.objects.get(job_id=job_id)
        request.user.job_set.remove(job)
        return
    else:
        render(request, 'jobs/unstar.html')