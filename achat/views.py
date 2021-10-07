
import datetime
from django.shortcuts import get_object_or_404, render, redirect
from paie.models import*

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime
import xlwt



@login_required


def indox(request):
          return render(request,'indox.html')





def export_excel111(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Ouled_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Od_berhil.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
########################################################
##########################################################

###########################################################
def export_excel222(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Ouled_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Od_drisse.objects.all().values_list(
                 'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response             

def export_excel333(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Aouloz.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel444(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=mariemo.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel555(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Rgaigue.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=rgaigueo.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response




def display11(request):
          if not request.user.is_authenticated:
                    return redirect('home')

          subjects=Od_berhil.objects.all()
          context={
           'subjects' : subjects,
           'header' : "Od_berhils"
          }
          return render(request,'indox.html',context)

def display22(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          subjects=Od_drisse.objects.all()
          context={
           'subjects' : subjects,
           'header' : "Od_drisses"
          }
          return render(request,'indox.html',context)

def display33(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          subjects=Aouloz.objects.all()
          context={
           'subjects' : subjects,
           'header' : "Aoulozs"
          }
          return render(request,'indox.html',context)



def edit_achat(request, pk, model, cls):
          if not request.user.is_authenticated:
                    return redirect('home')
          subject = get_object_or_404(model, pk=pk)
          if request.method == "POST":
                    form = cls(request.POST, instance=subject)
                    if form.is_valid():
                              form.save()
                              return redirect('indox')
          else:
                    form=cls(instance=subject)

                    return render(request,'modifier-item.html', {'form' : form})    
                        



def delete_desktop1(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Od_berhil.objects.filter(id=pk).delete()
          subjects=Od_berhil.objects.all()
          context={
                    'subjects' : subjects
          }
          return render(request,'indox.html', context)


def delete_laptop1(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Od_drisse.objects.filter(id=pk).delete()
          subjects=Od_drisse.objects.all()
          context={
                    'subjects' : subjects
          }
          return render(request,'indox.html', context)


def delete_mobile1(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Aouloz.objects.filter(id=pk).delete()
          subjects=Aouloz.objects.all()
          context={
                    'subjects' : subjects
          }
          return render(request,'indox.html', context)



