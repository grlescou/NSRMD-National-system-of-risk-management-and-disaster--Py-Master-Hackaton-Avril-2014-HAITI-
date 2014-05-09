#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django import forms
from gestionR.models import *
from django.forms.widgets import DateInput, SelectMultiple, CheckboxSelectMultiple, Select, RadioSelect
from gestionR.Data import *
#
# __author__ = 'Suy'

class EnqueteForm(forms.ModelForm):
    class Meta:
        model = Enquete
        exclude = ['datecreation','datemodification','user']
        widgets = {
            'debutenquete': DateInput(attrs={'type': 'date'}),
            'finenquete': DateInput(attrs={'type': 'date'}),
        }

class PerceptionForm(forms.ModelForm):
    risque = forms.CharField(widget=CheckboxSelectMultiple(choices=RISQUE))
    risqueseg = forms.CharField(widget=CheckboxSelectMultiple(choices=EFFETSEG))
    priorite1 = forms.CharField(widget=Select(choices=RISQUE))
    priorite2 = forms.CharField(widget=Select(choices=RISQUE))
    priorite3 = forms.CharField(widget=Select(choices=RISQUE))
    priorite4 = forms.CharField(widget=Select(choices=RISQUE))
    class Meta:
        model = Perception
        exclude = ['enquete','risques','local','risqueseg']
        widget = {
        }


class DegreDexpositionForm(forms.Form):
    choix = []

    # class Meta:
    #     model = DegreDexposition
    #     exclude = ['local','risque']
    # choix = [
    #     (c.id,c)for c in HtiAdm3.objects.all()
    # ]
    # localsd1 = forms.CharField(widget=SelectMultiple(choices=choix,attrs={'class':'chosen', 'style':'width:500px;'}))
    # localsd2 = forms.CharField(widget=SelectMultiple(choices=choix,attrs={'class':'chosen', 'style':'width:500px;'}))
    # localsd3 = forms.CharField(widget=SelectMultiple(choices=choix,attrs={'class':'chosen', 'style':'width:500px;'}))
    def __init__(self, *args, **kwargs):
        commune  = kwargs.pop('commune')
        super(DegreDexpositionForm, self).__init__(*args, **kwargs)
        choix = [
            (c.id,c)for c in HtiAdm3.objects.filter(id_2=commune.id)
        ]
        self.fields['localsd1'] = forms.CharField(widget=SelectMultiple(choices=choix,attrs={'class':'chosen', 'style':'width:500px;'}))
        self.fields['localsd2'] = forms.CharField(widget=SelectMultiple(choices=choix,attrs={'class':'chosen', 'style':'width:480px;'}))
        self.fields['localsd3'] = forms.CharField(widget=SelectMultiple(choices=choix,attrs={'class':'chosen', 'style':'width:500px;'}))
        self.fields['localsd1'].label = 'Fortement'
        self.fields['localsd2'].label = 'Modérément'
        self.fields['localsd3'].label = 'Faiblement'

# class DegreDexpositionForm(forms.ModelForm):
#     class Meta:
#         model = DegreDexposition
#         exclude = ['risque']
#     def __init__(self, *args, **kwargs):
#         commune  = kwargs.pop('commune')
#         super(DegreDexpositionForm, self).__init__(*args, **kwargs)
#         # choix = [
#         #     (c.id,c)for c in HtiAdm3.objects.filter(id_2=commune.id)
#         # ]
#         self.fields['local'].queryset = HtiAdm3.objects.filter(id_2=commune.id)


class VulnerabiliteForm(forms.Form):
    choix = []

    # class Meta:
    #     model = DegreDexposition
    #     exclude = ['local','risque']

    def __init__(self, *args, **kwargs):
        commune  = kwargs.pop('commune')
        super(VulnerabiliteForm, self).__init__(*args, **kwargs)
        choix = [
            (c.id,c)for c in HtiAdm3.objects.filter(id_2=commune.id)
        ]
        self.fields['localsd1'] = forms.CharField(widget=SelectMultiple(choices=choix,attrs={'class':'chosen', 'style':'width:500px;'}))
        self.fields['localsd2'] = forms.CharField(widget=SelectMultiple(choices=choix,attrs={'class':'chosen', 'style':'width:500px;'}))
        self.fields['localsd3'] = forms.CharField(widget=SelectMultiple(choices=choix,attrs={'class':'chosen', 'style':'width:500px;'}))
        self.fields['localsd1'].label = 'Fort'
        self.fields['localsd2'].label = 'Modéré'
        self.fields['localsd3'].label = 'Faible'



        # # class CommuneForm(ModelForm):
# #     class Meta:
# #         model = HaitiAdm3Stats
#
# class EnqueteForm(forms.Form):
#     choix = []
#     debutenquete = forms.DateTimeField(label="Début de l'enquête :",widget=DateInput(attrs={'type': 'date','class':'form-control'}))
#     finenquete = forms.DateTimeField(label="Fin de l'enquête :",widget=DateInput(attrs={'type': 'date','class':'form-control'}))
#     risque = forms.CharField(widget=SelectMultiple(choices=RISQUE))
#     risqueR = forms.CharField(widget=SelectMultiple(choices=()))
#     risqueseq = forms.CharField(widget=CheckboxSelectMultiple(choices=EFFETSEG))
#     priorite1 = forms.CharField(label="Risque prioritaire #1 :", widget=Select(choices=()))
#     priorite2 = forms.CharField(label="Risque prioritaire #2 :", widget=Select(choices=()))
#     priorite3 = forms.CharField(label="Risque prioritaire #3 :", widget=Select(choices=()))
#     priorite4 = forms.CharField(label="Risque prioritaire #4 :", widget=Select(choices=()))
#     degre = forms.CharField(label="degre d'exposition :",widget=Select(choices=DEGRE))
#     niveau = forms.CharField(label="Niveau :",widget=Select(choices=DEGRE))
#     section = forms.CharField(label="Sections Communales :")
#
#     def __init__(self, commune,*args, **kwargs):
#         super(EnqueteForm, self).__init__(*args, **kwargs)
#         self.commune = commune
#         l = HaitiAdm3Stats.objects.filter(commune=self.commune)
#         for s in l:
#             self.choix.append((s.id,s.section))
#
#         self.fields['section'].widget=Select(choices=self.choix)
#
#
#     def getCommune(self):
#         return self.commune
#
#
# class PresenceInstitutForm(forms.ModelForm):
#
#     class Meta:
#         model = PresenceInstitutionnelle
#         exclude = ['enquete']
#         widgets = {
#             'existenceclpc':RadioSelect(),
#         }
#
#
# class PlansCommunauxForm(forms.ModelForm):
#     class Meta:
#         model = PlansCommunaux
#         exclude = ['enquete']
#
#
# class MateriellesForm(forms.ModelForm):
#     class Meta:
#         model = HaitiAdm3Stats
#         exclude = ['enquete']
#
#
# class EquipementForm (forms.ModelForm):
#     class Meta:
#         model = HaitiAdm3Stats
#         exclude = ['enquete']
#
#
# class MoyenDeCommunicationForm(forms.ModelForm):
#     class Meta:
#         model = HaitiAdm3Stats
#         exclude = ['enquete']
#
#
#
#
# class MoyenDeTransportForm(forms.ModelForm):
#     class Meta:
#         model = HaitiAdm3Stats
#         exclude = ['enquete']
#
#
#
# class RessourceHumaineForm(forms.ModelForm):
#     class Meta:
#         model = HaitiAdm3Stats
#         exclude = ['enquete']
#
# class RessourceDInterventionForm(forms.ModelForm):
#     class Meta:
#         model = HaitiAdm3Stats
#         exclude = ['enquete']
#
#
# class EvaluationForm(forms.ModelForm):
#     class Meta:
#         model = HaitiAdm3Stats
#         exclude = ['enquete']