
from django import forms
from .models import *
from .models import *
from video.models import *



class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['titre',  'description', 'image']
        labels = {'titre': 'Titre',
                  'description': 'Description'}
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control mt-20'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

        }
class ArticleForm(forms.ModelForm):
              class Meta:
                    model = Article
                    fields = ['date','titre',  'description', 'image']
                    labels = {'date':'Date','titre': 'Domaine','description': 'Description'}
                    widgets = {
                     'date': forms.TextInput(attrs={'class': 'form-control mt-20'}),
                     'titre': forms.TextInput(attrs={'class': 'form-control mt-20'}),
                     'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

                       }


class DesktopForm(forms.ModelForm):
          class Meta:
              model = Ouled_berhil
              fields =('np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p')

class LaptopForm(forms.ModelForm):
          class Meta :
              model= Ouled_drisse
              fields =('np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p')


class MobileForm(forms.ModelForm):
          class Meta :
              model= Aoulouz
              fields =('np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p')



class DesktopFormo(forms.ModelForm):
          class Meta:
              model = Od_berhil
              fields =('desg', 'Qté', 'pu', 'pt')

class LaptopFormo(forms.ModelForm):
          class Meta :
              model= Od_drisse
              fields=('desg', 'Qté', 'pu', 'pt')


class MobileFormo(forms.ModelForm):
          class Meta :
              model= Aouloz
              fields=('desg', 'Qté', 'pu', 'pt')


class MariemFormo(forms.ModelForm):
          class Meta :
              model= mariemo
              fields=('desg', 'Qté', 'pu', 'pt')


class RgaigueFormo(forms.ModelForm):
          class Meta :
              model= rgaigueo
              fields=('desg', 'Qté', 'pu', 'pt')


class MariemForm(forms.ModelForm):
          class Meta :
              model= Mariem
              fields =('np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p')

class RgaigueForm(forms.ModelForm):
          class Meta :
              model= Rgaigue
              fields =('np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p')

class CaisseForm(forms.ModelForm):
          class Meta :
              model= Caisse              
              fields =('libelle','recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')



class EngraisBRForm(forms.ModelForm):
          class Meta :
              model= Engrais_berhil                         
              fields =('categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              
class EngraisDRForm(forms.ModelForm):
          class Meta :
              model= Engrais_drisse                         
              fields =('categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')


class EngraisAOForm(forms.ModelForm):
          class Meta :
              model = Engrais_Aoulouz                         
              fields =('categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')


class EngraisMRForm(forms.ModelForm):
          class Meta :
              model = Engrais_Mariem                        
              fields =('categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

class EngraisRGForm(forms.ModelForm):
          class Meta :
              model = Engrais_Rgaigue                        
              fields =('categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')



class StockSearchForm(forms.ModelForm):
              class Meta:
                  model = Engrais_berhil
                  fields = ['categorie','date']
                  
class ArticleSearchForm(forms.ModelForm):
              class Meta:
                  model = Article
                  fields = ['titre','date']

class PesticideBRForm(forms.ModelForm):
          class Meta :
              model= Pesticide_berhil                         
              fields =('category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')


class PesticideDRForm(forms.ModelForm):
          class Meta :
              model= Pesticide_drisse                        
              fields =('category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')


class PesticideAOForm(forms.ModelForm):
          class Meta :
              model= Pesticide_Aoulouz                    
              fields =('category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')





class StockSearchPSForm(forms.ModelForm):
              class Meta:
                  model = Pesticide_berhil
                  fields = ['category','date']
                  

class VideoForm(forms.ModelForm):              
    class Meta:                  
        model = Video        
        fields = ['caption','category','description', 'video']
        labels = {'caption': 'Titre' ,'category':'Categorie'}
        widgets = {
        'caption': forms.TextInput(attrs={'class': 'form-control mt-20'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            
        }





