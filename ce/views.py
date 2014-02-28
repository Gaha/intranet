#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.db.models import Sum
from ce.models import Agent, Commission, Activitee, Participation, Mendat

def view_agent(request) :
    reponse= {}
    reponse['list_agent'] = Agent.objects.all().order_by('nom')
    return render(request, 'agent.html', reponse)
    
def view_commission(request) :
    reponse = {}
    # liste des commissions
    reponse['list_commission'] = Commission.objects.all().order_by('nom')
    reponse['synth_commission'] = []
    for com in reponse['list_commission'] :
        reponse['synth_commission'].append({'commission' : com.nom, 'nb_activitee' : len(Activitee.objects.filter(commission__nom = com.nom)) })
    return render(request, 'commission.html', reponse)

def view_activitee(request) :
    reponse = {}
    reponse['list_activitee'] = Activitee.objects.all().order_by('commission__nom')
    # synthèse des activitées
    reponse['synth_activitee'] = []
    for acti in reponse['list_activitee'] :
        synth_acti = Participation.objects.filter( activitee__nom = acti.nom).aggregate(Sum('agent'),Sum('conjoint'),Sum('enfant'),Sum('externe'))
        synth_acti['activitee'] = acti.nom
        try :
            synth_acti['total'] = synth_acti['agent__sum'] + synth_acti['conjoint__sum'] + synth_acti['enfant__sum'] + synth_acti['externe__sum']
        except TypeError :
            synth_acti['total'] = 0
        reponse['synth_activitee'].append(synth_acti)
    #reponse['synth_activitee']['activitee'] = 'Les fourberies de scapin'
    return render(request, 'activitee.html', reponse)

def view_participation(request) :
    reponse = {}
    reponse['list_participation'] = Participation.objects.all().order_by('-activitee__date')
    return render(request, 'participation.html', reponse)
    
def membres_dup(request):
    reponse = {}

    # DUP
    try:
        reponse['dup_president'] = Mendat.objects.get(mendat = 'DUP_PR')
    except Mendat.DoesNotExist:
        reponse['dup_president'] = ''
    try:
        reponse['dup_secretaire'] = Mendat.objects.get(mendat = 'DUP_SE')
    except Mendat.DoesNotExist :
        reponse['dup_secretaire'] = ''
    # je pense que si je souhaite séparer les trésorier par une virgule, je doit le faire ici et pas dans le template
    reponse['dup_tresorier'] = Mendat.objects.filter(mendat = 'DUP_TR')
    reponse['dup_cadre_titu'] = Mendat.objects.filter(mendat = 'CA_TIT')
    reponse['dup_cadre_supp'] = Mendat.objects.filter(mendat = 'CA_SUP')
    reponse['dup_agent_titu'] = Mendat.objects.filter(mendat = 'AG_TIT')
    reponse['dup_agent_supp'] = Mendat.objects.filter(mendat = 'AG_SUP')

    # CHSCT
    try:
        reponse['chsct_president'] = Mendat.objects.get(mendat = 'CHS_PR')
    except Mendat.DoesNotExist:
        reponse['chsct_president'] = ''
    try:
        reponse['chsct_secretaire'] = Mendat.objects.get(mendat = 'CHS_SE')
    except Mendat.DoesNotExist :
        reponse['chsct_secretaire'] = ''
    reponse['chsct_membres'] = Mendat.objects.filter(mendat = 'CHS_ME')

    # DS
    reponse['ds_membres'] = Mendat.objects.filter(mendat = 'DS')


    return render(request, 'index.html', reponse)

