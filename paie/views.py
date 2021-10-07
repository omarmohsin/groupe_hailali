

from paie.forms import PesticideBRForm,PesticideDRForm,PesticideAOForm,EngraisBRForm, EngraisDRForm, EngraisAOForm
from django.shortcuts import get_object_or_404, render, redirect
from.models import*
#from achat.models import*
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from.forms import*
import xlwt
import datetime
from django.http import HttpResponse
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib import messages

def export_excel1(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Ouled_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Ouled_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Ouled_berhil.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
########################################################
##########################################################

###########################################################
def export_excel2(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Ouled_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Ouled_drisse.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response             

def export_excel3(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Aoulouz.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel4(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Mariem.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel5(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Rgaigue.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Rgaigue')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Rgaigue.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def home(request):
          title = 'Groupe Hailali'          
          return render(request,'home.html',{'title':title})


def local(request):
              if not request.user.is_authenticated:
                        return redirect('login-blog')
              list_articles = Article.objects.all()
              title = 'Liste des rapports'
              paginator = Paginator(list_articles, 12)
              page = request.GET.get('page')
              try:
                  items = paginator.page(page)
              except PageNotAnInteger:
                  items = paginator.page(1)
              except EmptyPage:
                  items = paginator.page(paginator.num_pages)


              index = items.number - 1
              max_index = len(paginator.page_range)
              start_index = index -5 if index >= 5 else 0
              end_index = index + 5 if index <= max_index - 5 else max_index
              page_range= paginator.page_range[start_index:end_index]
              context ={
                    'title':title,
                    'list_articles': list_articles,
                    'items': items,
                    'page_range': page_range,
                  }                  
              return render(request, "article.html", context)


def detail(request, pk):
              title = 'Detail de rapport'
              article = Article.objects.get(id=pk)         
              return render(request,'detail.html', {"article": article,'title':title})


@login_required
def index(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return render(request,'index.html')
def display1(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=Ouled_berhil.objects.all()
          subjects=Od_berhil.objects.all()
          context={  
                                   
                    'items' : items,
                    'subjects' : subjects,                   
                    'header' : "Ouled_berhils",
                    
          }
          return render(request,'index.html',context) 
          
                 
def display2(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=Ouled_drisse.objects.all()
          subjects=Od_drisse.objects.all()

          context={
                    'items' : items,
                    'subjects' : subjects,
                    'header' : "Ouled_drisses"
          }
          return render(request,'index.html',context)


def display3(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=Aoulouz.objects.all()
          subjects=Aouloz.objects.all()
          context={
                    'items' : items,
                    'subjects' : subjects,
                    'header' : "Aoulouzs"
          }
          return render(request,'index.html',context)


def display4(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=Mariem.objects.all()
          subjects=mariemo.objects.all()
          context={
                    'items' : items,
                    'subjects':subjects,
                    'header' : "Mariems"
          }
          return render(request,'index.html',context)

def display5(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=Rgaigue.objects.all()
          subjects=rgaigueo.objects.all()
          context={
                    'items' : items,
                    'subjects':subjects,
                    'header' : "Rgaigues"
          }
          return render(request,'index.html',context)

def add_employé(request,cls):
          if not request.user.is_authenticated:
                        return redirect('home')
          if request.method == "POST":
                    form = cls(request.POST)
                    if form.is_valid():
                              form.save()
                              return redirect('index')
          else:
                    form = cls()
                    return render(request,'add_new.html',{'form': form})
def add_desktop(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return add_employé(request,DesktopForm)
def add_laptop(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return add_employé(request,LaptopForm)
def add_mobile(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return add_employé(request,MobileForm)

def add_mariem(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return add_employé(request,MariemForm)

def add_rgaigue(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return add_employé(request,RgaigueForm)
###########################################################################
def add_depense(request,cls):
                   
          if request.method == "POST":
                    form = cls(request.POST)
                    if form.is_valid():
                              form.save()
                              return redirect('index')
          else:
                    form = cls()
          return render(request,'ajouter_nv.html',{'form': form})

def add_desktop1(request):
          return add_depense(request,DesktopFormo)

def add_laptop1(request):
          return add_depense(request,LaptopFormo)

def add_mobile1(request):
          return add_depense(request,MobileFormo)
def add_Mariema(request):
          return add_depense(request,MariemFormo)
def add_Rgaiguea(request):
          return add_depense(request,RgaigueFormo)
###########################################################################  


def edit_employé(request, pk, model, cls):
          if not request.user.is_authenticated:
                        return redirect('home')
          item = get_object_or_404(model, pk=pk)
          if request.method == "POST":
                    form = cls(request.POST, instance=item)
                    if form.is_valid():
                              form.save()
                              return redirect('index')
          else:
                    form=cls(instance=item)

                    return render(request,'edit_item.html', {'form' : form})  

def edit_desktop(request, pk):
          return edit_employé(request, pk, Ouled_berhil, DesktopForm)
def edit_laptop(request, pk):
          return edit_employé(request, pk, Ouled_drisse, LaptopForm)
def edit_mobile(request,pk):
          return edit_employé(request, pk, Aoulouz, MobileForm)
def edit_mariem(request,pk):
          return edit_employé(request, pk, Mariem, MariemForm)
def edit_rgaigue(request,pk):
          return edit_employé(request, pk, Rgaigue, RgaigueForm)


def edit_achat(request, pk, model, cls):
          if not request.user.is_authenticated:
                    return redirect('home')
          subject = get_object_or_404(model, pk=pk)
          if request.method == "POST":
                    form = cls(request.POST, instance=subject)
                    if form.is_valid():
                              form.save()
                              return redirect('index')
          else:
                    form=cls(instance=subject)

                    return render(request,'modifier-item.html', {'form' : form})
def edit_desktop1(request, pk):
          return edit_achat(request, pk, Od_berhil, DesktopFormo)

def edit_laptop1(request, pk):
          return edit_achat(request, pk, Od_drisse, LaptopFormo)

def edit_mobile1(request,pk):
          return edit_achat(request, pk, Aouloz, MobileFormo)
###################################################################
def delete_desktop(request, pk):
          Ouled_berhil.objects.filter(id=pk).delete()
          items=Ouled_berhil.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)

def delete_laptop(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          Ouled_drisse.objects.filter(id=pk).delete()
          items=Ouled_drisse.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)
def delete_mobile(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          Aoulouz.objects.filter(id=pk).delete()
          items=Aoulouz.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)

def delete_mariem(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          Mariem.objects.filter(id=pk).delete()
          items=Mariem.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)

def delete_rgaigue(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          Rgaigue.objects.filter(id=pk).delete()
          items=Rgaigue.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)


#############################################################
def caisse(request):             
          if not request.user.is_authenticated:
                        return redirect('home')
          title ='Gestion de la caisse'
          return render(request,'caisse.html',{'title':title})

def affiche(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items = Caisse.objects.all()          
          return render(request,'caisse.html',{'items':items})
"""""
#################################################################
#################################################################
#################################################################


          """""
def export_excel11(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Ouled_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_Ouled_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows= Engrais_berhil.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel22(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Ouled_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_drisse.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response             

def export_excel33(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_Aoulouz.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
def export_excel44(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_Mariem.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel55(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Rgaigue.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_Rgaigue')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_Rgaigue.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
              ##################################
def engrais(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return render(request,'engrais.html')
def display111(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          title = 'Liste de consommation des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_berhil.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "Engrais_berhils",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_berhil.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           date__icontains=form['date'].value()
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,

                  }                 
				                                 
          return render(request,'engrais.html',context)
def display222(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_drisse.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "Engrais_drisses",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_drisse.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           date__icontains=form['date'].value()
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,
                  }                 
				                                 
          return render(request,'engrais.html',context)
def display333(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_Aoulouz.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "Engrais_Aoulouzs",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_Aoulouz.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           date__icontains=form['date'].value()
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,

                  }                 				                                 
          return render(request,'engrais.html',context)
def display444(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          title = 'Liste de consommation des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_Mariem.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "Engrais_Mariems",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_Mariem.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           date__icontains=form['date'].value()
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,

                  }                 
				                                 
          return render(request,'engrais.html',context)
def display555(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_Rgaigue.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "Engrais_Rgaigues",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_Rgaigue.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           date__icontains=form['date'].value()
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,
                  }                 
				                                 
          return render(request,'engrais.html',context)
##########################################################################
# #######################################################################          
def add_consomation(request,cls):
          if not request.user.is_authenticated:
                        return redirect('home')         
          if request.method == "POST":
                    form = cls(request.POST)
                    if form.is_valid():
                              form.save()
                              return redirect('engrais')
          else:
                    form = cls()
          return render(request,'add_engrais.html',{'form': form})
def add_desktop111(request):
          return add_consomation(request,EngraisBRForm)

def add_laptop111(request):
          return add_consomation(request,EngraisDRForm)

def add_mobile111(request):
          return add_consomation(request,EngraisAOForm)


def edit_consomation(request, pk, model, cls):
          if not request.user.is_authenticated:
                    return redirect('home')
          subject = get_object_or_404(model, pk=pk)
          if request.method == "POST":
                    form = cls(request.POST, instance=subject)
                    if form.is_valid():
                              form.save()
                              return redirect('engrais')
          else:
                    form=cls(instance=subject)
                    return render(request,'modifier-item.html', {'form' : form})    
def edit_desktop111(request, pk):
          return edit_consomation(request, pk, Engrais_berhil, EngraisBRForm)
def edit_laptop111(request, pk):
          return edit_consomation(request, pk, Engrais_drisse, EngraisDRForm)
def edit_mobile111(request,pk):
          return edit_consomation(request, pk, Engrais_Aoulouz, EngraisAOForm)
def delete_desktop111(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Engrais_berhil.objects.filter(id=pk).delete()
          elements=Engrais_berhil.objects.all()
          context={
                    'elements' : elements
          }
          return render(request,'engrais.html', context)
def delete_laptop111(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Engrais_drisse.objects.filter(id=pk).delete()
          elements=Engrais_drisse.objects.all()
          context={
                    'elements' : elements
          }
          return render(request,'engrais.html', context)
def delete_mobile111(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Engrais_Aoulouz.objects.filter(id=pk).delete()
          elements=Engrais_Aoulouz.objects.all()
          context={
                     'elements' : elements
          }
          return render(request,'engrais.html', context)

"""""
#################################################################
#################################################################
#################################################################
"""""

def export_excel1111(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_Ouled_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_Ouled_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows= Pesticide_berhil.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel2222(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_Ouled_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_drisse.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response             

def export_excel3333(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_Aoulouz.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
def export_excel4444(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_Mariem.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel5555(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_Rgaigue.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_Rgaigue')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_Rgaigue.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response




def pesticide(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return render(request,'pesticide.html')
def display1111(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_berhil.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_berhils",
           "form": form,
          }
          if request.method == 'POST':                        
                  orderes = Pesticide_berhil.objects.filter(category__icontains=form['category'].value(),
                                                            date__icontains=form['date'].value()
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,
                  }  
          return render(request,'pesticide.html',context)
def display2222(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_drisse.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_drisses",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_drisse.objects.filter(category__icontains=form['category'].value(),
                                                            date__icontains=form['date'].value()
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,

                  }  
          return render(request,'pesticide.html',context)
def display3333(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_Aoulouz.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_Aoulouzs",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_Aoulouz.objects.filter(category__icontains=form['category'].value(),
                                                            date__icontains=form['date'].value()
                                                            )
                                                        
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,

                  }  
          return render(request,'pesticide.html',context)


def display4444(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_Mariem.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_Mariems",
           "form": form,
          }
          if request.method == 'POST':                        
                  orderes = Pesticide_Mariem.objects.filter(category__icontains=form['category'].value(),
                                                            date__icontains=form['date'].value()
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,
                  }  
          return render(request,'pesticide.html',context)
def display5555(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_Rgaigue.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_Rgaigues",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_Rgaigue.objects.filter(category__icontains=form['category'].value(),
                                                            date__icontains=form['date'].value()
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,

                  }  
          return render(request,'pesticide.html',context)
          ######################################################
################################################################
def add_consomme(request,cls):
          if not request.user.is_authenticated:
                        return redirect('home')         
          if request.method == "POST":
                    form = cls(request.POST)
                    if form.is_valid():
                              form.save()
                              return redirect('pesticide')
          else:
                    form = cls()
          return render(request,'add_engrais.html',{'form': form})
def add_desktop1111(request):
          return add_consomme(request,PesticideBRForm)
def add_laptop1111(request):
          return add_consomme(request,PesticideDRForm)
def add_mobile1111(request):
          return add_consomme(request,PesticideAOForm)
def edit_pesti(request, pk, model, cls):
          if not request.user.is_authenticated:
                    return redirect('home')
          subject = get_object_or_404(model, pk=pk)
          if request.method == "POST":
                    form = cls(request.POST, instance=subject)
                    if form.is_valid():
                              form.save()
                              return redirect('pesticide')
          else:
                    form=cls(instance=subject)

                    return render(request,'modifier-item.html', {'form' : form})    
def edit_desktop1111(request, pk):
          return edit_pesti(request, pk, Pesticide_berhil, PesticideBRForm)
def edit_laptop1111(request, pk):
          return edit_pesti(request, pk, Pesticide_drisse, PesticideDRForm)
def edit_mobile1111(request,pk):
          return edit_pesti(request, pk, Pesticide_Aoulouz, PesticideAOForm)
def delete_desktop1111(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Pesticide_berhil.objects.filter(id=pk).delete()
          orderes=Pesticide_berhil.objects.all()
          context={
                    'orderes' : orderes
          }
          return render(request,'pesticide.html', context)
def delete_laptop1111(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Pesticide_drisse.objects.filter(id=pk).delete()
          orderes=Pesticide_drisse.objects.all()
          context={
                    'orderes' : orderes
          }
          return render(request,'pesticide.html', context)
def delete_mobile1111(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Pesticide_Aoulouz.objects.filter(id=pk).delete()
          orderes=Pesticide_Aoulouz.objects.all()
          context={
                    'orderes' : orderes
          }
          return render(request,'pesticide.html', context)

###################################################################
###################################################################
def Ouvrier(request):
    if not request.user.is_authenticated:
                        return redirect('home')
    title = 'Liste des employés'
    list_personne=Personne.objects.all()
    paginator = Paginator(list_personne,12)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)


    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index -5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range= paginator.page_range[start_index:end_index]
    context ={
        'title':title,
        'list_personne': list_personne,
        'items': items,
        'page_range': page_range,
    }
    return render(request,'ouvriers.html',context)

###################################################################
###################################################################
class AddPersonne(CreateView):
          model=Personne
          form_class=PersonneForm
          template_name='add-ouv.html'
          success_url="/ouvriers"
          def form_valid(self,form):
          
                    form.instance.user=self.request.user
                    return super().form_valid(form)

class AddArticle(CreateView):
          model=Article
          form_class=ArticleForm
          template_name='ajouter-article.html'
          success_url="/public"

          def form_valid(self,form):
          
                    form.instance.user=self.request.user
                    return super().form_valid(form)  
#################################################################
###################################################################
#######################################################################

def caisse1(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_berhil.objects.all()
          
          context={  
                                   
                    'items' : items,
                                       
                    'header' : "caisse_berhils",
                    
          }
          return render(request,'caisse.html',context) 
          
                 
def caisse2(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_drisse.objects.all()
          

          context={
                    'items' : items,
                    
                    'header' : "caisse_drisses"
          }
          return render(request,'caisse.html',context)


def caisse3(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_Aoulouz.objects.all()
          
          context={
                    'items' : items,
                    
                    'header' : "caisse_Aoulouzs"
          }
          return render(request,'caisse.html',context)


def caisse4(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_Mariem.objects.all()
          
          context={
                    'items' : items,
                    
                    'header' : "caisse_Mariems"
          }
          return render(request,'caisse.html',context)

def caisse5(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_Rgaigue.objects.all()
          
          context={
                    'items' : items,
                    
                    'header' : "caisse_Rgaigues"
          }
          return render(request,'caisse.html',context)
#####################################################################
#####################################################################
#####################################################################

def export_caisse1(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_berhil.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
########################################################
########################################################
########################################################
def export_caisse2(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_drisse.objects.all().values_list('libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response             

def export_caisse3(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_Aoulouz.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_caisse4(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_Mariem.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_caisse5(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_Rgaigue.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_Rgaigue')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_Rgaigue.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response