#-*- coding:utf-8 -*-

from django.contrib import admin
from ce.models import Agent, Commission, Activitee, Participation, Mendat, CommissionMembre

class AgentAdmin(admin.ModelAdmin) :
    list_display = ('nom','prenom','contrat')
    list_filter = ('nom','prenom','contrat')
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

class MendatAdmin(admin.ModelAdmin) :
    list_display = ('nom','mendat')
    list_filter = ('mendat',)

class CommissionMembreAdmin(admin.ModelAdmin) :
    list_display = ('commission','agent','membre')
    list_filter = ('commission','membre')
    ordering = ('commission',)

admin.site.register(Agent, AgentAdmin)
admin.site.register(Commission)
admin.site.register(Activitee, ActiviteeAdmin)
admin.site.register(Participation, ParticipationAdmin)
admin.site.register(Mendat, MendatAdmin)
admin.site.register(CommissionMembre,CommissionMembreAdmin)
