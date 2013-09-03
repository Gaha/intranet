#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('ce.views',
    url(r'^$', 'membres_dup'),
    url(r'^agent', 'view_agent', name = 'agent'),
    url(r'^commission', 'view_commission', name = 'commission'),
    url(r'^activitee', 'view_activitee', name = 'activitee'),
    url(r'^participation', 'view_participation', name = 'participation'),
    )
