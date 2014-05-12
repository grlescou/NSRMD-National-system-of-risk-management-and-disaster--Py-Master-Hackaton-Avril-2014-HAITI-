from django.core.files.base import ContentFile
from gestionR.models import HtiAdm3, DegreDexposition, Vulnerabilite, Risque, FileWord, Perception
# import win32com.client
# import os
from django.core.files import File
from django.core.files.storage import default_storage
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
    def getrisque(self,id):
        return Risque.objects.get(id=id).risque

    def getpriorite(self,id):
        return Risque.objects.get(id=id).priorite

    def readdocfile(self,id):
        file_name = 'test.html'
        fileobjet = FileWord.objects.get(id=id)
        #word = win32com.client.gencache.EnsureDispatch("Word.Application")
        #doc = word.Documents.Open (fileobjet.file.path)
        # f = open(fileobjet.file.path, 'r')
        # # content_file = ContentFile(file_object.read())
        # myfile = File(f)
        # print myfile.readlines
        # print f.read(1)
        # myfile.close()
        # f.close()
        #
        # print fileobjet.file.path
        # doc.Close()
        t = 'hhhh'

        texts = default_storage.open(fileobjet.file.path).read()
        print texts
        content_file = ContentFile(texts)
        #fileobjet.file.save(file_name, content_file, save=True)

    def enqueterisque(self,id):
        for perception in Perception.objects.all():
            for risque in perception.risques.all():
                if(risque.id == id):
                    return perception.enquete.id
        return None


