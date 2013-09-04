#-*- coding:utf-8 -*-

from django.shortcuts import render
from ce.models import Agent, Commission, Activitee, Participation, Mendat

def view_agent(request) :
    reponse= {}
    reponse['list_agent'] = Agent.objects.all()
    return render(request, 'agent.html', reponse)
    
def view_commission(request) :
    reponse = {}
    # liste des commissions
    reponse['list_commission'] = Commission.objects.all()
    synthese = []
    for com in reponse['list_commission'] :
        synthese.append((com.nom, len(Activitee.objects.filter(commission__nom = com.nom))))
    reponse['synth_commission'] = synthese
    return render(request, 'commission.html', reponse)

def view_activitee(request) :
    reponse = {}
    reponse['list_activitee'] = Activitee.objects.all()
    return render(request, 'activitee.html', reponse)

def view_participation(request) :
    reponse = {}
    reponse['list_participation'] = Participation.objects.all()
    return render(request, 'participation.html', reponse)
    
def membres_dup(request):
    reponse = {}
    try :
        reponse['dup_president'] = Mendat.objects.get(mendat = 'DUP_PR')
    except :
        reponse['dup_president'] = ''
    try :
        reponse['dup_secretaire'] = Mendat.objects.get(mendat = 'DUP_SE')
    except Mendat.DoesNotExist :
        reponse['dup_secretaire'] = ''
    # je pense que si je souhaite séparer les trésorier par une virgule, je doit le faire ici et pas dans le template
    reponse['dup_tresorier'] = Mendat.objects.filter(mendat = 'DUP_TR')
    reponse['dup_cadre_titu'] = Mendat.objects.filter(mendat = 'CA_TIT')
    reponse['dup_cadre_supp'] = Mendat.objects.filter(mendat = 'CA_SUP')
    reponse['dup_agent_titu'] = Mendat.objects.filter(mendat = 'AG_TIT')
    reponse['dup_agent_supp'] = Mendat.objects.filter(mendat = 'AG_SUP')
    return render(request, 'index.html', reponse)
