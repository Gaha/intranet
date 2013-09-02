#-*- coding:utf-8 -*-

from django.views.generic import ListView
from django.views.generic import TemplateView
from ce.models import Agent, Commission, Activitee, Participation

class AgentView(ListView) :
    template_name = "agent.html"
    model = Agent

class AcceuilView(TemplateView) :
    template_name = "index.html"
    
class CommissionView(ListView) :
    template_name = "commission.html"
    model = Commission
    
class ActiviteeView(ListView) :
    template_name = "activitee.html"
    model = Activitee

class ParticipationView(ListView) :
    template_name = "participation.html"
    model = Participation
    
