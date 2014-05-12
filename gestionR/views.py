#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
#from esih_hackathon.models import  User,  Formulaire
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from gestionR.forms import *
import datetime
from django.contrib.auth.admin import Group

# Create your views here.
# from gestionR.forms import CommuneForm
# from gestionR.models import *
from gestionR.manager import DataManager
from gestionR.models import HtiAdm0, HtiAdm1, HtiAdm2, HtiAdm3, Vulnerabilite, Enquete, DegreDexposition, Risque, \
    Perception
from vectorformats.Formats import Django, GeoJSON
""" Home page """
def index(request):
    if not 'userid' in request.session:
        return redirect("/")
    # comms = HaitiAdm3Stats.objects.all()
    # for com in comms:
    #     try:
    #         Group(name=com.commune).save()
    #     except:
    #         pass

    if not 'userid' in request.session:
        return redirect("/")
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

""" list enquete """
def enquetes(request):
    if not 'userid' in request.session:
        return redirect("/")
    enquetes = Enquete.objects.all()
    return render_to_response('enquete/list.html', locals(), context_instance=RequestContext(request))

def jsonmapsallenquete(request):
    enquetes = Enquete.objects.all()
    query = []
    for enquete in enquetes:
        query.append(enquete.local)
    djf = Django.Django(geodjango="geom", properties=[])  #['commune','niveau','departemen','section']
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(query))
    return HttpResponse(s)

def mapsallenquete(request):
    if not 'userid' in request.session:
        return redirect("/")
    return render_to_response('enquete/map.html', locals(), context_instance=RequestContext(request))

def getRisque(liste,value):
    print liste
    print value
    if value in liste:
        return value
    return False

def formEnquete(request):
    if not 'userid' in request.session:
        return redirect("/")
    if request.method == 'GET':
        form = EnqueteForm(prefix='enquete')
        formp = PerceptionForm(prefix='perception')
    if request.method == 'POST':
        form = EnqueteForm(request.POST,prefix='enquete')
        formp = PerceptionForm(request.POST,prefix='perception')
        if form.is_valid() and formp.is_valid():
            enquete = form.save(commit=False)
            enquete.datecreation = datetime.datetime.now()
            enquete.datemodification = datetime.datetime.now()
            enquete.user_id = request.session['userid']
            enquete.save()

            perception = formp.save(commit=False)
            perception.enquete = enquete
            perception.risqueseg = formp.cleaned_data['risqueseg']

            priorite1 = getRisque(formp.cleaned_data['risque'],formp.cleaned_data['priorite1'])
            r1 = Risque(risque=priorite1,priorite=1)
            if getRisque(formp.cleaned_data['risque'],formp.cleaned_data['priorite2']):
                priorite2 = getRisque(formp.cleaned_data['risque'],formp.cleaned_data['priorite2'])

            r2 = Risque(risque=priorite2,priorite=2)
            if getRisque(formp.cleaned_data['risque'],formp.cleaned_data['priorite3']):
                priorite3 = getRisque(formp.cleaned_data['risque'],formp.cleaned_data['priorite3'])
            r3 = Risque(risque=priorite3,priorite=3)

            if getRisque(formp.cleaned_data['risque'],formp.cleaned_data['priorite4']):
                priorite4 = getRisque(formp.cleaned_data['risque'],formp.cleaned_data['priorite4'])
            r4 = Risque(risque=priorite4,priorite=4)
            r1.save()
            r2.save()
            r3.save()
            r4.save()
            perception.save()
            perception.risques.add(r1)
            perception.risques.add(r2)
            perception.risques.add(r3)
            perception.risques.add(r4)

            return redirect('/NextFormEnquete/{}/'.format(enquete.id))

    return render_to_response('enquete/form.html', locals(), context_instance=RequestContext(request))

def to_python(value):
        if not value:
            value = []

        if isinstance(value, list):
            return value
        return ast.literal_eval(value)
def formEnqueteNext(request,id):
     if not 'userid' in request.session:
         return redirect("/")
     if request.method == 'GET':
         enquete = Enquete.objects.get(id=id)
         perception = Perception.objects.get(enquete_id=id)
         formr1 = DegreDexpositionForm(commune=enquete.local,prefix='formr1')

         formr2 = DegreDexpositionForm(commune=enquete.local,prefix='formr2')
         formr3 = DegreDexpositionForm(commune=enquete.local,prefix='formr3')
         formr4 = DegreDexpositionForm(commune=enquete.local,prefix='formr4')

         formvr1 = VulnerabiliteForm(commune=enquete.local,prefix='formvr1')
         formvr2 = VulnerabiliteForm(commune=enquete.local,prefix='formvr2')
         formvr3 = VulnerabiliteForm(commune=enquete.local,prefix='formvr3')
         formvr4 = VulnerabiliteForm(commune=enquete.local,prefix='formvr4')
     if request.method == 'POST':
         enquete = Enquete.objects.get(id=id)
         perception = Perception.objects.get(enquete_id=id)
         formr1 = DegreDexpositionForm(request.POST,commune=enquete.local,prefix='formr1')
         vformr1 = formr1.is_valid()
         formr2 = DegreDexpositionForm(request.POST,commune=enquete.local,prefix='formr2')
         vformr2 = formr2.is_valid()
         formr3 = DegreDexpositionForm(request.POST,commune=enquete.local,prefix='formr3')
         vformr3 = formr3.is_valid()
         formr4 = DegreDexpositionForm(request.POST,commune=enquete.local,prefix='formr4')
         vformr4 = formr4.is_valid()

         formvr1 = VulnerabiliteForm(request.POST,commune=enquete.local,prefix='formvr1')
         vformvr1 = formvr1.is_valid()
         formvr2 = VulnerabiliteForm(request.POST,commune=enquete.local,prefix='formvr2')
         vformvr2 = formvr2.is_valid()
         formvr3 = VulnerabiliteForm(request.POST,commune=enquete.local,prefix='formvr3')
         vformvr3 = formvr3.is_valid()
         formvr4 = VulnerabiliteForm(request.POST,commune=enquete.local,prefix='formvr4')
         vformvr4 = formvr4.is_valid()
         if formr1.is_valid() and formr2.is_valid() and formr3.is_valid() and formr4.is_valid() and formvr1.is_valid() and formvr2.is_valid() and formvr3.is_valid() and formvr4.is_valid():
             # pr = formr1.cleaned_data['localsd1'].split()
             # print pr
             # for l in pr:
             #     print l
             # return HttpResponse(list(formr1.cleaned_data['localsd1']))
             #---------------------------------------------------------------------------
             #-----------Save degre d'exposition et vlnerabilite a risque priorite 1---------------------
             #---------------------------------------------------------------------------
             r1 = perception.risques.get(priorite=1)
             for local in to_python(formr1.cleaned_data['localsd1']):
                d = DegreDexposition(degre='Fortement',risqued=r1,local=HtiAdm3.objects.get(id=int(local)))
                d.save()
             for local in to_python(formr1.cleaned_data['localsd2']):
                d = DegreDexposition(degre='Modérément',risqued=r1,local=HtiAdm3.objects.get(id=int(local)))
                d.save()
             for local in to_python(formr1.cleaned_data['localsd3']):
                d = DegreDexposition(degre='Faiblement',risqued=r1,local=HtiAdm3.objects.get(id=int(local)))
                d.save()

                                        #...................Save degre d'exposition.......
             for local in to_python(formvr1.cleaned_data['localsd1']):
                v = Vulnerabilite(niveau='Fort',risquev=r1,local=HtiAdm3.objects.get(id=int(local)))
                v.save()
             for local in to_python(formvr1.cleaned_data['localsd2']):
                v = Vulnerabilite(niveau='Modéré',risquev=r1,local=HtiAdm3.objects.get(id=int(local)))
                v.save()
             for local in to_python(formvr1.cleaned_data['localsd3']):
                v = Vulnerabilite(niveau='Faible',risquev=r1,local=HtiAdm3.objects.get(id=int(local)))
                v.save()


             #---------------------------------------------------------------------------
             #-----------Save degre d'exposition et vlnerabilite a risque priorite 2---------------------
             #---------------------------------------------------------------------------
             r2 = perception.risques.get(priorite=2)
             for local in to_python(formr2.cleaned_data['localsd1']):
                d = DegreDexposition(degre='Fortement',risqued=r2,local=HtiAdm3.objects.get(id=int(local)))
                d.save()
             for local in to_python(formr2.cleaned_data['localsd2']):
                d = DegreDexposition(degre='Modérément',risqued=r2,local=HtiAdm3.objects.get(id=int(local)))
                d.save()
             for local in to_python(formr2.cleaned_data['localsd3']):
                d = DegreDexposition(degre='Faiblement',risqued=r2,local=HtiAdm3.objects.get(id=int(local)))
                d.save()

                                        #...................Save vulnerabilite.......
             for local in to_python(formvr2.cleaned_data['localsd1']):
                v = Vulnerabilite(niveau='Forte',risquev=r2,local=HtiAdm3.objects.get(id=int(local)))
                v.save()
             for local in to_python(formvr2.cleaned_data['localsd2']):
                v = Vulnerabilite(niveau='Modéré',risquev=r2,local=HtiAdm3.objects.get(id=int(local)))
                v.save()
             for local in to_python(formvr2.cleaned_data['localsd3']):
                v = Vulnerabilite(niveau='Faible',risquev=r2,local=HtiAdm3.objects.get(id=int(local)))
                v.save()

             #---------------------------------------------------------------------------
             #-----------Save degre d'exposition et vlnerabilite a risque priorite 3---------------------
             #---------------------------------------------------------------------------
             r3 = perception.risques.get(priorite=3)
                                        #...................Save degre d'exposition.......
             for local in to_python(formr3.cleaned_data['localsd1']):
                d = DegreDexposition(degre='Fortement',risqued=r3,local=HtiAdm3.objects.get(id=int(local)))
                d.save()
             for local in to_python(formr3.cleaned_data['localsd2']):
                d = DegreDexposition(degre='Modérément',risqued=r3,local=HtiAdm3.objects.get(id=int(local)))
                d.save()
             for local in to_python(formr3.cleaned_data['localsd3']):
                d = DegreDexposition(degre='Faiblement',risqued=r3,local=HtiAdm3.objects.get(id=int(local)))
                d.save()

                                        #...................Save vulnerabilite.......
             for local in to_python(formvr3.cleaned_data['localsd1']):
                v = Vulnerabilite(niveau='Forte',risquev=r3,local=HtiAdm3.objects.get(id=int(local)))
                v.save()
             for local in to_python(formvr3.cleaned_data['localsd2']):
                v = Vulnerabilite(niveau='Modéré',risquev=r3,local=HtiAdm3.objects.get(id=int(local)))
                v.save()
             for local in to_python(formvr3.cleaned_data['localsd3']):
                v = Vulnerabilite(niveau='Faible',risquev=r3,local=HtiAdm3.objects.get(id=int(local)))
                v.save()



             #---------------------------------------------------------------------------
             #-----------Save degre d'exposition et vlnerabilite a risque priorite 4---------------------
             #---------------------------------------------------------------------------
             r4 = perception.risques.get(priorite=4)
             for local in to_python(formr4.cleaned_data['localsd1']):
                d = DegreDexposition(degre='Fortement',risqued=r4,local=HtiAdm3.objects.get(id=int(local)))
                d.save()
             for local in to_python(formr4.cleaned_data['localsd2']):
                d = DegreDexposition(degre='Modérément',risqued=r4,local=HtiAdm3.objects.get(id=int(local)))
                d.save()
             for local in to_python(formr4.cleaned_data['localsd3']):
                d = DegreDexposition(degre='Faiblement',risqued=r4,local=HtiAdm3.objects.get(id=int(local)))
                d.save()

                                        #...................Save vulnerabilite.......
             for local in to_python(formvr4.cleaned_data['localsd1']):
                v = Vulnerabilite(niveau='Forte',risquev=r4,local=HtiAdm3.objects.get(id=int(local)))
                v.save()
             for local in to_python(formvr4.cleaned_data['localsd2']):
                v = Vulnerabilite(niveau='Modéré',risquev=r4,local=HtiAdm3.objects.get(id=int(local)))
                v.save()
             for local in to_python(formvr4.cleaned_data['localsd3']):
                v = Vulnerabilite(niveau='Faible',risquev=r4,local=HtiAdm3.objects.get(id=int(local)))
                v.save()
             perception.enquete.complete = True
             perception.enquete.save()
             return redirect('/Enquetes')
         # else:

         #     return HttpResponse("Error")

     return render_to_response('enquete/nextform.html',locals(),context_instance=RequestContext(request))

     ##if request.method == 'POST':



def presenceinstitutionnelle(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    enquete = Enquete.objects.get(id=id)
    presences = PresenceInstitutionnelle.objects.filter(enquete_id=id)
    if request.method=='GET':
        enquete = Enquete.objects.get(id=id)
        form = PresenceInstitutForm(commune=enquete.local)
    if request.method=='POST':
        enquete = Enquete.objects.get(id=id)
        form = PresenceInstitutForm(request.POST,commune=enquete.local)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enquete = Enquete.objects.get(id=id)
            instance.save()

        return redirect("/PresenceInstutionnelle/{}/".format(id))
    return render_to_response('enquete/presenceinstitutionelle.html', locals(), context_instance=RequestContext(request))


def plansCommunauxForm(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    enquete = Enquete.objects.get(id=id)
    plans = PlansCommunaux.objects.filter(enquete_id=id)
    if request.method=='GET':
        enquete = Enquete.objects.get(id=id)
        form = PlansCommunauxForm()
    if request.method=='POST':
        enquete = Enquete.objects.get(id=id)
        form = PlansCommunauxForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enquete = Enquete.objects.get(id=id)
            instance.save()
    return render_to_response('enquete/plan.html', locals(), context_instance=RequestContext(request))


def materiels(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    enquete = Enquete.objects.get(id=id)
    materiels = Materielles.objects.filter(enquete_id=id)
    if request.method=='GET':
        enquete = Enquete.objects.get(id=id)
        form = MateriellesForm()
    if request.method=='POST':
        enquete = Enquete.objects.get(id=id)
        form = MateriellesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enquete = Enquete.objects.get(id=id)
            instance.save()
    return render_to_response('enquete/materiels.html', locals(), context_instance=RequestContext(request))




def equipements(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    enquete = Enquete.objects.get(id=id)
    equipements = Equipement.objects.filter(enquete_id=id)
    if request.method=='GET':
        enquete = Enquete.objects.get(id=id)
        form = EquipementForm()
    if request.method=='POST':
        enquete = Enquete.objects.get(id=id)
        form = EquipementForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enquete = Enquete.objects.get(id=id)
            instance.save()
    return render_to_response('enquete/equipements.html', locals(), context_instance=RequestContext(request))

def communications(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    enquete = Enquete.objects.get(id=id)
    communications = MoyenDeCommunication.objects.filter(enquete_id=id)
    if request.method=='GET':
        enquete = Enquete.objects.get(id=id)
        form = MoyenDeCommunicationForm()
    if request.method=='POST':
        enquete = Enquete.objects.get(id=id)
        form = MoyenDeCommunicationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enquete = Enquete.objects.get(id=id)
            instance.save()
    return render_to_response('enquete/communications.html', locals(), context_instance=RequestContext(request))


def tranports(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    enquete = Enquete.objects.get(id=id)
    transports = MoyenDeTransport.objects.filter(enquete_id=id)
    if request.method=='GET':
        enquete = Enquete.objects.get(id=id)
        form = MoyenDeTransportForm()
    if request.method=='POST':
        enquete = Enquete.objects.get(id=id)
        form = MoyenDeTransportForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enquete = Enquete.objects.get(id=id)
            instance.save()
    return render_to_response('enquete/transports.html', locals(), context_instance=RequestContext(request))


def ressourceshumaines(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    enquete = Enquete.objects.get(id=id)
    ressources = RessourceHumaine.objects.filter(enquete_id=id)
    if request.method=='GET':
        enquete = Enquete.objects.get(id=id)
        form = RessourceHumaineForm()
    if request.method=='POST':
        enquete = Enquete.objects.get(id=id)
        form = RessourceHumaineForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enquete = Enquete.objects.get(id=id)
            instance.save()
    return render_to_response('enquete/ressources.html', locals(), context_instance=RequestContext(request))


def interventions(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    enquete = Enquete.objects.get(id=id)
    interventions = RessourceDIntervention.objects.filter(enquete_id=id)
    if request.method=='GET':
        enquete = Enquete.objects.get(id=id)
        form = RessourceDInterventionForm()
    if request.method=='POST':
        enquete = Enquete.objects.get(id=id)
        form = RessourceDInterventionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enquete = Enquete.objects.get(id=id)
            instance.save()
    return render_to_response('enquete/intervention.html', locals(), context_instance=RequestContext(request))

def evaluations(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    enquete = Enquete.objects.get(id=id)
    evaluations = Evaluation.objects.filter(enquete_id=id)
    if request.method=='GET':
        enquete = Enquete.objects.get(id=id)
        form = EvaluationForm()
    if request.method=='POST':
        enquete = Enquete.objects.get(id=id)
        form = EvaluationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.enquete = Enquete.objects.get(id=id)
            instance.save()
    return render_to_response('enquete/evaluations.html', locals(), context_instance=RequestContext(request))


def sections(request):
    # if not 'userid' in request.session:
    #     return redirect("/")
    # sections = HaitiAdm3Stats.objects.filter(request.session['commune'])
    return render_to_response('enquete/sections.html', locals(), context_instance=RequestContext(request))

def carto (request):
    # try:
        # if 'User' not in request.session :
        #     return redirect("/admindesktop/loginPage/")

    html = get_template('gestionR/carto.html')
    return HttpResponse(html.render(Context()))
    # except :
    #     t = get_template('404Error.html')
    #     html = t.render(Context({'info': 'Erreur dans la page'}))
    #     return HttpResponse(html)

def addcommune(request):
    #form = CommuneForm()
    return render_to_response('editcommune.html', locals(), context_instance=RequestContext(request))

def editcommune(request,id):
    if not 'userid' in request.session:
        return redirect("/")
    # haitiAdm3Stats = HaitiAdm3Stats.objects.get(id=id)
    # form = CommuneForm(instance=haitiAdm3Stats)
    return render_to_response('editcommune.html', locals(), context_instance=RequestContext(request))

def jsonmapbase(request):
    query = HtiAdm1.objects.all()
    djf = Django.Django(geodjango="geom", properties=['id_0'])  #['commune','niveau','departemen','section']
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(query))
    return HttpResponse(s)

def jsonsectionmaps(request):
    query = HtiAdm3.objects.all()
    # for zip in query:
    #     zip.geom.srid = 4326
    #     zip.geom.transform(900913)
        #zip.save()

    # i = 1
    # for q in query:
    #     try:
    #         print str(i)+" "
    #         print q.geom
    #         i = i + 1
    #         if i > 4:
    #             break
    #     except:
    #         break
    djf = Django.Django(geodjango="geom", properties=[])  #['commune','niveau','departemen','section']
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(query))
    return HttpResponse(s)


def jsoncomnmaps(request):
    com = request.GET['com']
    # query =HaitiAdm3Stats.objects.filter(departemen='OUEST')
    # for zip in query:
    #     zip.geom.srid = 4326
    #     zip.geom.transform(900913)
        #zip.save()

    # i = 1
    # for q in query:
    #     try:
    #         print str(i)+" "
    #         print q.geom
    #         i = i + 1
    #         if i > 4:
    #             break
    #     except:
    #         break
    # djf = Django.Django(geodjango="geom", properties=['commune','departemen'])  #['commune','niveau','departemen','section']
    # geoj = GeoJSON.GeoJSON()
    # s = geoj.encode(djf.decode(query))
    return HttpResponse('s')


def viewmaps(request):
    if not 'userid' in request.session:
        return redirect("/")
    return render_to_response('viewmap.html', locals(), context_instance=RequestContext(request))

def viewmapsCom(request):
    if not 'userid' in request.session:
        return redirect("/")
    return render_to_response('viewmapCom.html', locals(), context_instance=RequestContext(request))


# def viewmaps(request):
#     if not 'userid' in request.session:
#         return redirect("/")
#     return render_to_response('viewmap.html', locals(), context_instance=RequestContext(request))

def zoneVulnerable(request):
    vulnerabilites = Vulnerabilite.objects.all()
    if 'n' in request.GET:
        try:
            if request.GET['n']=='0':
               vulnerabilites = Vulnerabilite.objects.filter(niveau='Faible')
               n = '0'
            if request.GET['n']=='1':
               vulnerabilites = Vulnerabilite.objects.filter(niveau='Modéré')
               n = '1'
            if request.GET['n']=='2':
               vulnerabilites = Vulnerabilite.objects.filter(niveau='Fort')
               n = '2'
        except ValueError:
            pass
    return render_to_response('vulnerabilite/list.html', locals(), context_instance=RequestContext(request))
def jsonzoneVulnerable(request):
    vulnerabilites = Vulnerabilite.objects.all()
    if 'n' in request.GET:
        try:
            if request.GET['n']=='0':
               vulnerabilites = Vulnerabilite.objects.filter(niveau='Faible')
               n = '0'
            if request.GET['n']=='1':
               vulnerabilites = Vulnerabilite.objects.filter(niveau='Modéré')
               n = '1'
            if request.GET['n']=='2':
               vulnerabilites = Vulnerabilite.objects.filter(niveau='Fort')
               n = '2'
        except ValueError:
            pass
    query = []
    for vulnerabilite in vulnerabilites:
        query.append(vulnerabilite.local)
    djf = Django.Django(geodjango="geom", properties=[])  #['commune','niveau','departemen','section']
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(query))
    return HttpResponse(s)
def mapzoneVulnerable(request):
    if 'n' in request.GET:
        try:
            if request.GET['n']=='0':
               n = '0'
            if request.GET['n']=='1':
               n = '1'
            if request.GET['n']=='2':
               n = '2'
        except ValueError:
            pass
    return render_to_response('vulnerabilite/map.html', locals(), context_instance=RequestContext(request))



def degreDexposition(request):
    degreDexpositions = DegreDexposition.objects.all()
    titletable = 'faiblement, modérément et fortement'
    if 'd' in request.GET:
        try:
            if request.GET['d']=='0':
               degreDexpositions = DegreDexposition.objects.filter(degre='Faiblement')
               titletable = 'faiblement'
               d = '0'
            if request.GET['d']=='1':
               degreDexpositions = DegreDexposition.objects.filter(degre='Modérément')
               titletable = 'modérément'
               d = '1'
            if request.GET['d']=='2':
               degreDexpositions = DegreDexposition.objects.filter(degre='Fortement')
               titletable = 'fortement'
               d = '2'
        except ValueError:
            pass
    return render_to_response('degredexposition/list.html', locals(), context_instance=RequestContext(request))
def jsondegreDexposition(request):
    degreDexpositions = DegreDexposition.objects.all()
    if 'd' in request.GET:
        try:
            if request.GET['d']=='0':
               degreDexpositions = DegreDexposition.objects.filter(degre='Faiblement')
               d = '0'
            if request.GET['d']=='1':
               degreDexpositions = DegreDexposition.objects.filter(degre='Modérément')
               d = '1'
            if request.GET['d']=='2':
               degreDexpositions = DegreDexposition.objects.filter(degre='Fortment')
               d = '2'
        except ValueError:
            pass
    query = []
    for degreDexposition in degreDexpositions:
        query.append(degreDexposition.local)
    djf = Django.Django(geodjango="geom", properties=[])  #['commune','niveau','departemen','section']
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(query))
    return HttpResponse(s)
def mapdegreDexposition(request):
    if 'd' in request.GET:
        try:
            if request.GET['d']=='0':
               d = '0'
            if request.GET['d']=='1':
               d = '1'
            if request.GET['d']=='2':
               d = '2'
        except ValueError:
            pass
    return render_to_response('degredexposition/map.html', locals(), context_instance=RequestContext(request))




def risques(request):
    zones = HtiAdm3.objects.raw('SELECT * FROM public."hti_adm3" INNER JOIN public."gestionR_degredexposition" ON public."hti_adm3".id=public."gestionR_degredexposition".local_id INNER JOIN  public."gestionR_vulnerabilite" ON public."hti_adm3".id=public."gestionR_vulnerabilite".local_id;')
    # for p in HtiAdm3.objects.raw('SELECT * FROM public."gestionR_vulnerabilite" INNER JOIN public."gestionR_degredexposition" ON public."gestionR_vulnerabilite".risque_id=public."gestionR_degredexposition".risque_id;'):
    #     print p.name_3
    # zones = Perception.objects
    dataManager = DataManager()
    titletable = '1, 2, 3 et 4'
    if 'd' in request.GET:
        try:
            if request.GET['p']=='1':
               # zones = Risque.objects.filter(priorite=1)
               titletable = '1'
               p = '1'
            if request.GET['p']=='2':
               # zones = Risque.objects.filter(priorite=2)
               titletable = '2'
               p = '2'
            if request.GET['p']=='3':
               # zones = Risque.objects.filter(priorite=3)
               titletable = '3'
               p = '3'
            if request.GET['p']=='4':
               # zones = Risque.objects.filter(priorite=4)
               titletable = '4'
               p = '4'
        except ValueError:
            pass
    return render_to_response('risque/list.html', locals(), context_instance=RequestContext(request))


def jsonrisques(request):
    sql = """SELECT * FROM public."hti_adm3" INNER JOIN public."gestionR_degredexposition"
ON public."hti_adm3".id=public."gestionR_degredexposition".local_id
INNER JOIN  public."gestionR_vulnerabilite" ON public."hti_adm3".id=public."gestionR_vulnerabilite".local_id
INNER JOIN public."gestionR_risque" ON public."gestionR_risque".id=public."gestionR_vulnerabilite".risquev_id;
"""


    # AND public."gestionR_risque".id=public."gestionR_degredexposition".risqued_id;
    query = HtiAdm3.objects.raw(sql)
    djf = Django.Django(geodjango="geom", properties=['name_1','name_2','name_3', 'degre', 'niveau','risque'])  #['commune','niveau','departemen','section']
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(query))
    return HttpResponse(s)



def jsonrisquesdegreeexposition(request):
    sql = """SELECT * FROM public."hti_adm3" INNER JOIN public."gestionR_degredexposition"
ON public."hti_adm3".id=public."gestionR_degredexposition".local_id
INNER JOIN public."gestionR_risque" ON public."gestionR_risque".id=public."gestionR_vulnerabilite".risquev_id;
"""


    # AND public."gestionR_risque".id=public."gestionR_degredexposition".risqued_id;
    query = HtiAdm3.objects.raw(sql)
    djf = Django.Django(geodjango="geom", properties=['name_1','name_2','name_3', 'degre', 'niveau','risque'])  #['commune','niveau','departemen','section']
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(query))
    return HttpResponse(s)



def jsonrisquesvulnerabilite(request):
    sql = """SELECT * FROM public."hti_adm3" INNER JOIN  public."gestionR_vulnerabilite" ON public."hti_adm3".id=public."gestionR_vulnerabilite".local_id
INNER JOIN public."gestionR_risque" ON public."gestionR_risque".id=public."gestionR_vulnerabilite".risquev_id;
"""


    # AND public."gestionR_risque".id=public."gestionR_degredexposition".risqued_id;
    query = HtiAdm3.objects.raw(sql)
    djf = Django.Django(geodjango="geom", properties=['name_1','name_2','name_3', 'degre', 'niveau','risque'])  #['commune','niveau','departemen','section']
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(query))
    return HttpResponse(s)






def maprisque(request):
    return render_to_response('risque/map.html', locals(), context_instance=RequestContext(request))

def jsonRisquesection(request):
    sql = """SELECT public."gestionR_risque".id, public."gestionR_risque".risque FROM public."gestionR_risque"
             INNER JOIN public."gestionR_vulnerabilite" ON public."gestionR_risque".id=public."gestionR_vulnerabilite".risquev_id
             AND public."gestionR_vulnerabilite".local_id=23
             INNER JOIN public."gestionR_degredexposition" ON public."gestionR_risque".id=public."gestionR_degredexposition".risqued_id
             AND public."gestionR_degredexposition".local_id=23"""
    query = HtiAdm3.objects.raw(sql)
    data = {}
    l = []
    for item in query:
        l.append(str(item))
    data['data']=l
    print data

    return HttpResponse(json.dumps(data, ensure_ascii=False))



def jsondegreDexposition(request):
    degreDexpositions = DegreDexposition.objects.all()
    if 'd' in request.GET:
        try:
            if request.GET['d']=='0':
               degreDexpositions = DegreDexposition.objects.filter(degre='Faiblement')
               d = '0'
            if request.GET['d']=='1':
               degreDexpositions = DegreDexposition.objects.filter(degre='Modérément')
               d = '1'
            if request.GET['d']=='2':
               degreDexpositions = DegreDexposition.objects.filter(degre='Fortment')
               d = '2'
        except ValueError:
            pass
    query = []
    for degreDexposition in degreDexpositions:
        query.append(degreDexposition.local)
    djf = Django.Django(geodjango="geom", properties=[])  #['commune','niveau','departemen','section']
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(query))
    return HttpResponse(s)

def mapdegreDexposition(request):
    if 'd' in request.GET:
        try:
            if request.GET['d']=='0':
               d = '0'
            if request.GET['d']=='1':
               d = '1'
            if request.GET['d']=='2':
               d = '2'
        except ValueError:
            pass
    return render_to_response('degredexposition/map.html', locals(), context_instance=RequestContext(request))


def zoneArisque(request):
    return render_to_response('viewmapCom.html', locals(), context_instance=RequestContext(request))

def zoneArisqueparpriorite(request):
    return render_to_response('viewmapCom.html', locals(), context_instance=RequestContext(request))
