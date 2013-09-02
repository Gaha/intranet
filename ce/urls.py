#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url

from ce.views import *

urlpatterns = patterns('',
    url(r'^$', AcceuilView.as_view(), name = 'agent'),
    url(r'^agent', AgentView.as_view(), name = 'acceuil'),
    url(r'^commission', CommissionView.as_view(), name = 'commission'),
    url(r'^activitee', ActiviteeView.as_view(), name = 'activitee'),
    url(r'^participation', ParticipationView.as_view(), name = 'participation'),
    )
