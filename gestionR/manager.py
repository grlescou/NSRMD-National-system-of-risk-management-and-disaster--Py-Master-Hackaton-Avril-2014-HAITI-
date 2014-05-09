from gestionR.models import HtiAdm3, DegreDexposition, Vulnerabilite

__author__ = 'Suy'

class DataManager():
    def risque(self):
        data = {}
        for local in HtiAdm3.objects.all():
            # data[local.id] = []
            lv = None
            for v in Vulnerabilite.objects.all():
                if v.local.id==local.id:
                    lv=v
            ld = None
            for d in DegreDexposition.objects.all():
                if d.local.id==local.id:
                    ld=d
            data[local.id] = (local,ld,lv)
        return data

