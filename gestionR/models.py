#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import ast
from django.contrib.auth.models import User

from django.contrib.gis.db import models


class HtiAdm0(models.Model):
    id = models.IntegerField(primary_key=True)
    id_0 = models.IntegerField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True)
    name_engli = models.CharField(max_length=50, blank=True)
    name_iso = models.CharField(max_length=54, blank=True)
    name_fao = models.CharField(max_length=50, blank=True)
    name_local = models.CharField(max_length=54, blank=True)
    name_obsol = models.CharField(max_length=150, blank=True)
    name_varia = models.CharField(max_length=160, blank=True)
    name_nonla = models.CharField(max_length=50, blank=True)
    name_frenc = models.CharField(max_length=50, blank=True)
    name_spani = models.CharField(max_length=50, blank=True)
    name_russi = models.CharField(max_length=50, blank=True)
    name_arabi = models.CharField(max_length=50, blank=True)
    name_chine = models.CharField(max_length=50, blank=True)
    waspartof = models.CharField(max_length=100, blank=True)
    contains = models.CharField(max_length=50, blank=True)
    sovereign = models.CharField(max_length=40, blank=True)
    iso2 = models.CharField(max_length=4, blank=True)
    www = models.CharField(max_length=2, blank=True)
    fips = models.CharField(max_length=6, blank=True)
    ison = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    validfr = models.CharField(max_length=12, blank=True)
    validto = models.CharField(max_length=10, blank=True)
    eumember = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    objects = models.GeoManager()
    class Meta:
        # managed = False
        db_table = 'hti_adm0'

class HtiAdm1(models.Model):
    id = models.IntegerField(primary_key=True)
    id_0 = models.IntegerField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True)
    name_0 = models.CharField(max_length=75, blank=True)
    id_1 = models.IntegerField(blank=True, null=True)
    name_1 = models.CharField(max_length=75, blank=True)
    nl_name_1 = models.CharField(max_length=50, blank=True)
    varname_1 = models.CharField(max_length=150, blank=True)
    type_1 = models.CharField(max_length=50, blank=True)
    engtype_1 = models.CharField(max_length=50, blank=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    objects = models.GeoManager()
    class Meta:
        # managed = False
        db_table = 'hti_adm1'

class HtiAdm2(models.Model):
    id = models.IntegerField(primary_key=True)
    id_0 = models.IntegerField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True)
    name_0 = models.CharField(max_length=75, blank=True)
    id_1 = models.IntegerField(blank=True, null=True)
    name_1 = models.CharField(max_length=75, blank=True)
    id_2 = models.IntegerField(blank=True, null=True)
    name_2 = models.CharField(max_length=75, blank=True)
    nl_name_2 = models.CharField(max_length=75, blank=True)
    varname_2 = models.CharField(max_length=150, blank=True)
    type_2 = models.CharField(max_length=50, blank=True)
    engtype_2 = models.CharField(max_length=50, blank=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    objects = models.GeoManager()
    class Meta:
        # managed = False
        db_table = 'hti_adm2'
    def __unicode__(self):
        return '%s' % self.name_2

class HtiAdm3(models.Model):
    id = models.IntegerField(primary_key=True)
    id_0 = models.IntegerField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True)
    name_0 = models.CharField(max_length=75, blank=True)
    id_1 = models.IntegerField(blank=True, null=True)
    name_1 = models.CharField(max_length=75, blank=True)
    id_2 = models.IntegerField(blank=True, null=True)
    name_2 = models.CharField(max_length=75, blank=True)
    id_3 = models.IntegerField(blank=True, null=True)
    name_3 = models.CharField(max_length=75, blank=True)
    nl_name_3 = models.CharField(max_length=75, blank=True)
    varname_3 = models.CharField(max_length=100, blank=True)
    type_3 = models.CharField(max_length=50, blank=True)
    engtype_3 = models.CharField(max_length=50, blank=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    objects = models.GeoManager()
    class Meta:
        # managed = False
        db_table = 'hti_adm3'

    def __unicode__(self):
        return '%s' % self.name_3






class Enquete(models.Model):
    datecreation = models.DateField()
    datemodification = models.DateField()
    debutenquete = models.DateField()
    finenquete = models.DateField()
    local = models.ForeignKey(HtiAdm2)
    user = models.ForeignKey(User)
    complete = models.BooleanField(default=False)



class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class Risque(models.Model):
    risque = models.CharField(max_length=100)
    priorite = models.PositiveIntegerField()
    # def local(self):
    #     for vulnerabilite in




class DegreDexposition(models.Model):
    DEGRE = (
        (u'Fortement',u'Fortement'),
        (u'Modérément',u'Modérément'),
        (u'Faiblement',u'Faiblement'),
    )
    degre = models.CharField(max_length=100,choices=DEGRE)
    risqued = models.ForeignKey(Risque)
    local = models.ForeignKey(HtiAdm3)

class Vulnerabilite(models.Model):
    NIVEAU = (
        (u'Fort',u'Fort'),
        (u'Modéré',u'Modéré'),
        (u'Faible',u'Faible'),
    )
    niveau = models.CharField(max_length=50,choices=NIVEAU)
    local = models.ForeignKey(HtiAdm3)
    risquev = models.ForeignKey(Risque)


class Perception(models.Model):
    enquete = models.ForeignKey(Enquete)
    risqueseg = ListField()
    risques = models.ManyToManyField(Risque)
    def perception(self):
        vulnerabilite = Vulnerabilite.objects.all()


class PresenceInstitutionnelle(models.Model):
    EXISTENCE = (
        (u'Oui',u'Oui'),
        (u'Non',u'Non'),
    )
    local = models.ForeignKey(HtiAdm3)
    enquete = models.ForeignKey(Enquete)
    existenceclpc = models.CharField("Existence de CLPC :",max_length=50,choices=EXISTENCE,default=None)
    def resultat(self):
        if self.existenceclpc.__eq__(self.EXISTENCE[0][1]):
            return float(1)/float(len(HtiAdm3.objects.filter(id_2=self.local.id_2)))*100
        else:
            return 0
    def objectif(self):
        return float(1)/float(len(HtiAdm3.objects.filter(id_2=self.local.id_2)))*100
    def perception(cls,id):
        for p in PresenceInstitutionnelle.objects.all():
            if p.id == id:
                return  p
        return None




class PlansCommunaux(models.Model):
    EXISTENCE = (
        (u'Oui et actualisé',u'Oui et actualisé'),
        (u'Oui mais non actualisé',u'Oui mais non actualisé'),
        (u'Non',u'Non'),
    )
    TYPE = (
        (u'Plan de réponse communale',u'Plan de réponse communale'),
        (u'Plan de diffusion de l\'alerte',u'Plan de diffusion de l\'alerte'),
        (u'Plan de communication',u'Plan de communication'),
        (u'Plan d\'évacuation',u'Plan d\'évacuation'),
    )
    enquete = models.ForeignKey(Enquete)
    type = models.CharField("Type",max_length=300,choices=TYPE)
    existenceplan = models.CharField("Existence du plan",max_length=150,choices=EXISTENCE)
    def resultat(self):
        if self.existenceplan.__eq__(self.EXISTENCE[2][1]):
            return 0.00 * 100
        elif self.existenceplan.__eq__(self.EXISTENCE[0][1]):
            return 0.125 * 100
        else:
            return 0.25 * 100
    def objectif(self):
        return 0.25*100

class Materielles(models.Model):
    TYPE = (
        (u'Espace de réunion/Centre d\'opération',u'Espace de réunion/Centre d\'opération'),
        (u'Dépôt',u'Dépôt'),
        (u'Abris temporaires',u'Abris temporaires'),
    )
    EXISTENCE = (
        (u'Oui et adéquat',u'Oui et adéquat'),
        (u'Oui mais pas adéquat',u'Oui mais pas adéquat'),
        (u'Non',u'Non'),
    )
    enquete = models.ForeignKey(Enquete)
    type = models.CharField(max_length=300,choices=TYPE)
    existence = models.CharField(max_length=300,choices=EXISTENCE)
    def resultat(self):
        if self.existence.__eq__(self.EXISTENCE[2][1]):
            return 0.00 * 100
        elif self.existence.__eq__(self.EXISTENCE[1][1]):
            return 0.1667 * 100
        else:
            return 0.3333 * 100

    def objectif(self):
        return 0.3333 * 100


class Equipement(models.Model):
    TYPE = (
        (u'Génératrice',u'Génératrice'),
        (u'Imprimante',u'Imprimante'),
        (u'Ordinateurs',u'Ordinateurs'),
        (u'Matériels de déblaiement',u'Matériels de déblaiement'),
    )
    enquete = models.ForeignKey(Enquete)
    type = models.CharField(max_length=100,choices=TYPE)
    quantitedisponible = models.PositiveIntegerField("Quantité disponible")
    quantitenecessaire = models.PositiveIntegerField("Quantité nécessaire")
    def resultat(self):
        return (float(self.quantitedisponible)/float(self.quantitenecessaire)) * 0.25
    def objectif(self):
        return 0.25 * 100

class MoyenDeCommunication(models.Model):
    TYPE = (
        (u'Téléphone fixe',u'Téléphone fixe'),
        (u'Radio communication',u'Radio communication'),
        (u'Téléphone cellulaire',u'Téléphone cellulaire'),
        (u'Internet',u'Internet'),
    )
    enquete = models.ForeignKey(Enquete)
    type = models.CharField(max_length=300,choices=TYPE)
    quantitedisponible = models.PositiveIntegerField("Quantité disponible")
    quantitenecessaire = models.PositiveIntegerField("Quantité nécessaire")
    def resultat(self):
        return (float(self.quantitedisponible/self.quantitenecessaire)) * 0.25
    def objectif(self):
        return 0.25 * 100

class MoyenDeTransport(models.Model):
    TYPE = (
        (u'Véhicule tout terrain',u'Véhicule tout terrain'),
        (u'Bateaux',u'Bateaux'),
        (u'Motos',u'Motos'),
        (u'Camions',u'Camions'),
        (u'Ambulances',u'Ambulances'),
    )
    enquete = models.ForeignKey(Enquete)
    type = models.CharField(max_length=300,choices=TYPE)
    quantitedisponible = models.PositiveIntegerField("Quantité disponible")
    quantitenecessaire = models.PositiveIntegerField("Quantité nécessaire")
    def resultat(self):
        return (float(self.quantitedisponible)/float(self.quantitenecessaire)) * 0.2
    def objectif(self):
        return 0.2 * 100

class RessourceHumaine(models.Model):
    TYPE = (
        (u'COU',u'COU'),
        (u'PLANIF. URG.**',u'PLANIF. URG.**'),
        (u'EDAB***',u'EDAB***'),
        (u'ABRI PROV.****',u'ABRI PROV****'),
        (u'EDUC. & SENSIB.',u'EDUC. & SENSIB.'),
        (u'CARTES RISQUE',u'CARTES RISQUE'),
        (u'ALERTE PRECOCE',u'ALERTE PRECOCE'),
        (u'PROTO. COMMUNIC.',u'PROTO. COMMUNIC.'),
        (u'GESTION PROJET',u'GESTION PROJET'),
    )
    enquete = models.ForeignKey(Enquete)
    type = models.CharField(max_length=50,choices=TYPE)
    quantitedisponible = models.PositiveIntegerField("Quantité disponible")
    quantitenecessaire = models.PositiveIntegerField("Quantité nécessaire")
    def resultat(self):
        return (float(self.quantitedisponible)/float(self.quantitenecessaire)) * (float(1)/float(9))
    def objectif(self):
        return 0.1 * 100

class RessourceDIntervention(models.Model):
    PRESENCE = (
        (u'Oui',u'Oui'),
        (u'Non',u'Non'),
    )
    TYPE = (
        (u'Brigadiers',u'Brigadiers'),
        (u'EIC',u'EIC'),
        (u'Pompiers',u'Pompiers'),
    )
    enquete = models.ForeignKey(Enquete)
    type = models.CharField(max_length=100,choices=TYPE)
    presence = models.CharField(max_length=10,choices=PRESENCE)
    def resultat(self):
        if self.presence.__eq__(self.PRESENCE[0][0]):
            return 0.3333 * 100
        else:
            return 0.00 * 100

    def objectif(self):
        return 0.3333 * 100

class Evaluation(models.Model):
    enquete = models.ForeignKey(Enquete)
    observations = models.TextField()
    objectif = models.TextField()
    def resultat(self):
        return 0.25

