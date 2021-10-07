from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

cat_choice = (
		('Ammonitrate', 'Ammonitrate'),
		('Sulfat_potasse', 'Sulfat_potasse'),
		('MAP', 'MAP'),
                    ('Nitrat_potasse', 'Nitrat_potasse'),
		('Calcium', 'Calcium'),
		('Complet', 'Complet'),
                    ('Acide', 'Acide'),
                    ('Sequestrine', 'Sequestrine'),
                    ('Uree_46', 'Uree_46'),
                    ('Kimia', 'Kimia'),
	)


class Engrais(models.Model):
          categorie = models.CharField(max_length=50, blank=True, null=True,choices=cat_choice)         
          date=models.CharField(max_length=100, blank=True)
          entree=models.CharField(max_length=100, blank=False)
          cumul_entree=models.CharField(max_length=100, blank=False)
          sortie=models.CharField(max_length=100, blank=False)
          cumul_sortie=models.CharField(max_length=100, blank=False)
          stock=models.CharField(max_length=100, blank=False)
          

          class Meta:
                    abstract = True

          def __str__(self):
                    return self.categorie
          
class Engrais_berhil(Engrais):
          pass

class Engrais_drisse(Engrais):
          pass

class Engrais_Aoulouz(Engrais):
          pass

class Engrais_Mariem(Engrais):
          pass

class Engrais_Rgaigue(Engrais):
          pass
#**********************************************************************
catag_choice = (
		('Karaté', 'Karaté'),
		('Blouz', 'Blouz'),
		('AG3', 'AG3'),
                    ('Agrale', 'Agrale'),
		('Coperniko', 'Coperniko'),
		('Confidor', 'Confidor'),
                    ('Valmec', 'Valmec'),
                    ('Joker', 'Joker'),
                    ('Pixel', 'Pixel'),
                    ('Coperide', 'Coperide'),
                    ('Mospelan', 'Mospelan'),
                    ('Rondo', 'Rondo'),
                    ('Fozika', 'Fozika'),
                    ('Movinto', 'Movinto'),
                    ('enfidor-speed', 'enfidor-speed'),
                    ('Magnome', 'Magnome'),
                    ('Mamba', 'Mamba'),
                    ('Fozika_ca', 'Fozika_ca'),
                    ('Soufre', 'Soufre'),
	)

class Pesticide(models.Model):
          category = models.CharField(max_length=50, blank=True, null=True,choices=catag_choice)         
          date=models.CharField(max_length=100, blank=True)
          entree=models.CharField(max_length=100, blank=False)
          cumul_entree=models.CharField(max_length=100, blank=False)
          sortie=models.CharField(max_length=100, blank=False)
          cumul_sortie=models.CharField(max_length=100, blank=False)
          stock=models.CharField(max_length=100, blank=False)
          

          class Meta:
                    abstract = True

          def __str__(self):
                    return self.category
          
class Pesticide_berhil(Pesticide):
          pass

class Pesticide_drisse(Pesticide):
          pass

class Pesticide_Aoulouz(Pesticide):
          pass

class Pesticide_Mariem(Pesticide):
          pass

class Pesticide_Rgaigue(Pesticide):
          pass


#************************************************************************************

class Semaine(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          np=models.CharField(max_length=100, blank=True)
          sdb=models.CharField(max_length=100, blank=False)
          j1=models.CharField(max_length=100, blank=False)
          j2=models.CharField(max_length=100, blank=False)
          j3=models.CharField(max_length=100, blank=False)
          j4=models.CharField(max_length=100, blank=False)
          j5=models.CharField(max_length=100, blank=False)
          j6=models.CharField(max_length=100, blank=False)
          j7=models.CharField(max_length=100, blank=False)
          nb_j=models.FloatField(max_length=100, blank=False)
          base=models.FloatField(max_length=100, blank=False)
          ancienneté=models.FloatField(max_length=100, blank=False)
          pf=models.FloatField(max_length=100, blank=False)
          sb=models.FloatField(max_length=100, blank=False)
          cnss=models.FloatField(max_length=100, blank=False)
          amo=models.FloatField(max_length=100, blank=False)
          net_p=models.FloatField(max_length=100, blank=False)
          class Meta:
                    abstract = True
          def __str__(self):
                    return self.np        
class Ouled_berhil(Semaine):
          pass
class Ouled_drisse(Semaine):
          pass
class Aoulouz(Semaine):
          pass
class Mariem(Semaine):
          pass
class Rgaigue(Semaine):
          pass
#**************************************************************************************
class Caisse(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          libelle=models.CharField(max_length=100,blank=True)
          recette=models.CharField(max_length=100,blank=True)
          cumul_recette=models.CharField(max_length=100,blank=True)
          depense=models.CharField(max_length=100,blank=True)
          cumul_depense=models.CharField(max_length=100,blank=True)
          solde=models.CharField(max_length=100,blank=True)
          
          
                  
          class Meta:
                    abstract = True
          def __str__(self):
                    return self.libelle        
class caisse_berhil(Caisse):
          pass
class caisse_drisse(Caisse):
          pass
class caisse_Aoulouz(Caisse):
          pass
class caisse_Mariem(Caisse):
          pass
class caisse_Rgaigue(Caisse):
          pass

class Achat(models.Model):
                   
          desg=models.CharField(max_length=100, blank=False)
          Qté=models.CharField(max_length=100, blank=False)
          pu=models.CharField(max_length=100, blank=False)
          pt=models.CharField(max_length=100, blank=False)
          

          class Meta:
                    abstract = True

          def __str__(self):
                    return self.desg
          
class Od_berhil(Achat):
          pass

class Od_drisse(Achat):
          pass

class Aouloz(Achat):
          pass

class mariemo(Achat):
          pass

class rgaigueo(Achat):
          pass



















class Personne(models.Model):              
              titre=models.CharField(max_length=50)    
              description=models.TextField()
              image=models.ImageField(null=True,blank=True)

              def __str__(self):
                              return self.titre



class Article(models.Model):         
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          date=models.CharField(max_length=100, blank=True)
          titre=models.CharField(max_length=50,blank=True)
          description=models.TextField()
          image=models.ImageField(null=True,blank=False)
          created_at = models.DateTimeField(auto_now_add=True)
          update_at = models.DateTimeField(auto_now=True)
          times = models.DateTimeField(auto_now_add=True, auto_now=False)
          

          def __str__(self):
               return self.titre
          def get_absolute_url(self):
                  return reverse("my_articles")