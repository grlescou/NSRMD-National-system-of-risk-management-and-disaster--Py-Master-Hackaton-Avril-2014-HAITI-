from django.conf.urls import patterns, include, url

from django.contrib import admin
import gestionR

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'users.views.login', name='index'),
    url(r'^Home$', 'gestionR.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', include(include('gestionR.urls'))),
    url(r'^android/', include(include('android_root.urls'))),
    url(r'^Enquetes$','gestionR.views.enquetes'),
    url(r'^FormEnquete$','gestionR.views.formEnquete'),
    url(r'^NextFormEnquete/(\d+)/$','gestionR.views.formEnqueteNext'),
    url(r'^PresenceInstutionnelle/(\d+)/$','gestionR.views.presenceinstitutionnelle'),
    url(r'^Plan/(\d+)/$','gestionR.views.plansCommunauxForm'),
    url(r'^Materiels/(\d+)/$','gestionR.views.materiels'),
    url(r'^Equipements/(\d+)/$','gestionR.views.equipements'),
    url(r'^MoyenCommunications/(\d+)/$','gestionR.views.communications'),
    url(r'^Transports/(\d+)/$','gestionR.views.tranports'),
    url(r'^RessourcesHumaines/(\d+)/$','gestionR.views.ressourceshumaines'),
    url(r'^RessourcesDIntervention/(\d+)/$','gestionR.views.interventions'),
    url(r'^Evaluation/(\d+)/$','gestionR.views.evaluations'),
    url(r'^Sections$','gestionR.views.sections'),
    url(r'^logout$','users.views.logout'),
)
