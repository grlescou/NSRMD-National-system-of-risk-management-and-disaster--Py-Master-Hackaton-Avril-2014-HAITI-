from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geoDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),editcommune
    url(r'^carto/', 'gestionR.views.carto', name='carto'),
    url(r'^addcommune/$', 'gestionR.views.addcommune', name='addcommune'),
    url(r'^editcommune/(\d+)/$', 'gestionR.views.editcommune', name='editcommune'),
    url(r'^viewmaps/$', 'gestionR.views.viewmaps', name='viewmaps'),
    url(r'^jsonsectionmaps/$', 'gestionR.views.jsonsectionmaps', name='jsonsectionmaps'),
    url(r'^jsonmapsallenquete/$', 'gestionR.views.jsonmapsallenquete', name='jsonmapsallenquete'),
    url(r'^Mapsallenquete/$', 'gestionR.views.mapsallenquete', name='mapsallenquete'),

    url(r'^jsonmapbase/$', 'gestionR.views.jsonmapbase', name='jsonmapbase'),

    url(r'^ZoneVulnerable$', 'gestionR.views.zoneVulnerable', name='zoneVulnerable'),
    url(r'^jsonzoneVulnerable/$', 'gestionR.views.jsonzoneVulnerable', name='jsonzoneVulnerable'),
    url(r'^MapzoneVulnerable/$', 'gestionR.views.mapzoneVulnerable', name='mapzoneVulnerable'),

    url(r'^DegreDexposition$', 'gestionR.views.degreDexposition', name='degreDexposition'),
    url(r'^jsondegreDexposition/$', 'gestionR.views.jsondegreDexposition', name='jsondegreDexposition'),
    url(r'^MapdegreDexposition/$', 'gestionR.views.mapdegreDexposition', name='mapdegreDexposition'),

    url(r'^Risques$', 'gestionR.views.risques', name='risques'),
    url(r'^jsonrisques/$', 'gestionR.views.jsonrisques', name='jsonrisques'),
    url(r'^MapRisque/$', 'gestionR.views.maprisque', name='maprisque'),
    url(r'^jsonRisquesection/$', 'gestionR.views.jsonRisquesection', name='jsonRisquesection'),

    url(r'^com/$', 'gestionR.views.viewmapsCom', name='viewmapsCom'),
    url(r'^jsoncommaps/$', 'gestionR.views.jsoncomnmaps', name='jsoncommaps'),

)

