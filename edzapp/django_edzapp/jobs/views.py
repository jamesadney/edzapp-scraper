from datetime import date, timedelta
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from jobs.models import Job


def index(request):
    jobs = Job.objects.exclude(deadline=None).filter(deadline__gte=date.today()).order_by("deadline")

    six_months_ago = date.today() - timedelta(weeks=26)
    no_deadlines = Job.objects.exclude(date_posted=None).exclude(
        date_posted__lt=six_months_ago).exclude(date_posted__gt=date.today()).filter(deadline=None).order_by("-date_posted")

    try:
        starred_jobs = request.user.job_set.order_by("deadline")
    except AttributeError:
        starred_jobs = None
    return render(request, 'jobs/index.html', {"jobs": jobs,
                                               "no_deadlines": no_deadlines,
                                               "starred_jobs": starred_jobs})


def all(request):
    return render(request, 'jobs/all.html')


def saved(request):
    return render(request, 'jobs/saved.html')


def detail(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    return render(request, 'jobs/detail.html', {"job": job})


def star(request, job_id):
    # TODO: fix csrf
    if request.method == 'POST':
        job = Job.objects.get(job_id=job_id)
        request.user.job_set.add(job)
        data = json.dumps({'type': 'star', 'job_id': job_id})
        response = HttpResponse(data, mimetype='application/json')
        return response
    else:
        return render(request, 'jobs/star.html')


def unstar(request, job_id):
    if request.method == 'POST':
        job = Job.objects.get(job_id=job_id)
        request.user.job_set.remove(job)
        data = json.dumps({'type': 'unstar', 'job_id': job_id})
        response = HttpResponse(data, mimetype='application/json')
        return response
    else:
        return render(request, 'jobs/unstar.html')
