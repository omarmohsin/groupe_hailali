from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(Personne)
admin.site.register(Article)

@admin.register(Ouled_berhil,Ouled_drisse,Aoulouz,Mariem,Rgaigue)
class ViewAdmin(ImportExportModelAdmin):
          pass
class OuledberhilAdmin(ImportExportModelAdmin):
          list_display=('id','np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p')

@admin.register(caisse_berhil,caisse_drisse,caisse_Aoulouz,caisse_Mariem,caisse_Rgaigue)
class CaisseAdmin(ImportExportModelAdmin):
          pass

@admin.register(Engrais_berhil,Engrais_drisse,Engrais_Aoulouz,Engrais_Mariem,Engrais_Rgaigue)
class ViewAdmin(ImportExportModelAdmin):
          pass

@admin.register(Pesticide_berhil,Pesticide_drisse,Pesticide_Aoulouz,Pesticide_Mariem,Pesticide_Rgaigue)
class ViewAdmin(ImportExportModelAdmin):
          pass
@admin.register(Od_berhil,Od_drisse,Aouloz, mariemo, rgaigueo)
class ViewAdmin(ImportExportModelAdmin):
          pass


