#-*- coding:utf-8 -*-

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Agent(models.Model):
    LISTE_CONTRAT = (
        ('CDI','CDI'),
        ('CDD','CDD'),
        ('PRE','Prestataire'),
        ('INT','Intérime'),
    )

    nom = models.CharField(max_length = 50)
    prenom = models.CharField(max_length = 50)
    contrat = models.CharField(max_length = 3, choices=LISTE_CONTRAT, default='CDI')
    
    # c'est ce qui s'affiche quand on print, notament dans admin
    def __unicode__(self) :
        return u'%s %s' % (self.nom, self.prenom)

class Mendat(models.Model) :
    LISTE_MENDAT = (
        ('DUP_PR','DUP Président'),
        ('DUP_SE','DUP Secrétaire'),
        ('CA_TIT','DUP Cadre Titulaire'),
        ('CA_SUP','DUP Cadre Suppléant'),
        ('AG_TIT','DUP Agent Titulaire'),
        ('AG_SUP','DUP Agent Suppléant'),
        ('DS','Délégués Syndical'),
        ('CHS_PR','CHSCT Président'),
        ('CHS_SE','CHSCT Secrétaire'),
        ('CHS_ME','CHSCT Membres'),
    )
    nom = models.ForeignKey('Agent')
    mendat = models.CharField(max_length = 6, choices=LISTE_MENDAT)

    def __unicode__(self) :
        return u'%s - %s' %(self.nom, self.mendat)

class Commission(models.Model):
    nom = models.CharField(max_length = 50)
    
    def __unicode__(self) :
        return u'%s' %(self.nom)

class CommissionMembre(models.Model) :
    LISTE_MEMBRE = (
        ('PRE','Président'),
        ('DUP','Membre DUP'),
        ('AGE','Membre Agent')
    )
    commission = models.ForeignKey('Commission')
    agent = models.ForeignKey('Agent')
    membre = models.CharField(max_length = 3, choices=LISTE_MEMBRE)

    def __unicode__(self) :
        return u'%s : %s - %s' %(self.commission, self.agent, self.membre)


class Activitee(models.Model):
    nom = models.CharField(max_length = 50)
    commission = models.ForeignKey('Commission')
    date = models.DateField()
    heure = models.TimeField()
    
    def __unicode__(self) :
        return u'%s : %s' % (self.date, self.nom)

class Participation(models.Model) :
    LISTE_ETAT = (
        ('IN','Inscrit'),
        ('AN','Annuler'),
    )
    nom = models.ForeignKey('Agent')
    activitee = models.ForeignKey('Activitee')
    agent = models.IntegerField(default = 1)
    conjoint = models.IntegerField(default = 0)
    enfant = models.IntegerField(default = 0)
    externe = models.IntegerField(default = 0)
    etat = models.CharField(max_length = 2, choices=LISTE_ETAT, default='IN')
    
    def __unicode__(self):
        return u'%s : %s' % (self.activitee, self.nom)
