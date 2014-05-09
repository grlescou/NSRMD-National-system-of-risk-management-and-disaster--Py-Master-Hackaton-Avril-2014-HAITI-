

# Register your models here.
from django.contrib.gis import admin
from gestionR.models import HtiAdm0

admin.site.register(HtiAdm0, admin.GeoModelAdmin)

