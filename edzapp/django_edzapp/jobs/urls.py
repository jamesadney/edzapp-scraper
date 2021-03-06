from django.conf.urls import patterns, url

urlpatterns = patterns(
    'jobs.views',
    url(r'^$', 'index'),
    url(r'^all/$', 'all'),
    url(r'^saved/$', 'saved'),
    url(r'^(?P<job_id>\d+)/$', 'detail'),
    url(r'^(?P<job_id>\d+)/star/$', 'star'),
    url(r'^(?P<job_id>\d+)/unstar/$', 'unstar'),
)
