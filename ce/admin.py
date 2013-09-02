#-*- coding:utf-8 -*-

from django.contrib import admin
from ce.models import Agent, Commission, Activitee, Participation

class AgentAdmin(admin.ModelAdmin) :
    list_display = ('nom','prenom')
    list_filter = ('nom','prenom')
    ordering = ('nom',)
    search_fields = ('nom','prenom')

class ActiviteeAdmin(admin.ModelAdmin) :
    list_display = ('date','commission','nom')
    list_filter = ('date','commission','nom')
    date_hierarchy = ('date')
    ordering = ('date',)
    search_fields = ('commission','nom')
    
class ParticipationAdmin(admin.ModelAdmin) :
    list_display = ('nom','activitee','agent','enfant','conjoint','externe','etat')
    list_filter = ('nom','activitee')
    ordering = ('activitee','nom')
    search_fields = ('nom', 'activitee')

admin.site.register(Agent, AgentAdmin)
admin.site.register(Commission)
admin.site.register(Activitee, ActiviteeAdmin)
admin.site.register(Participation, ParticipationAdmin)
