from django.shortcuts import render, redirect

from django.urls import reverse
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from paie.models import Article
from paie.forms import ArticleForm, ArticleSearchForm





@login_required

def user_article(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          title = 'Liste des rapports'             
          has_perm= False
          if request.user.has_perm("project.delete_article"):
                    has_perm= True
          
          list_articles= Article.objects.all()
          form = ArticleSearchForm(request.POST or None)
          if request.method == 'POST':          
                  list_articles= Article.objects.filter(titre__icontains=form['titre'].value(),
                                                        date__icontains=form['date'].value()
                                                        )
                                                                             
          return render(request,'my-articles.html',{'list_articles':list_articles,"has_perm":has_perm,'form':form, 'title':title})
#####################################################################
def bilan(request, id_article):
          article = Article.objects.get(id=id_article)         
          return render(request,'bilan.html', {"article": article})






class AddArticle(LoginRequiredMixin,CreateView):
          model=Article
          form_class=ArticleForm
          template_name='ajouter-article.html'
          success_url="/my-admin/my-articles" 


          def form_valid(self,form):

                    form.instance.user=self.request.user
                    return super().form_valid(form)

class UpdateArticle(LoginRequiredMixin,UpdateView):
          model = Article
          form_class= ArticleForm
          template_name ='app_admin/article_form.html'
          success_url ="/my-admin/my-articles"
          
class DeleteArticle(DeleteView):
          model = Article          
          success_url ="/my-admin/my-articles"

          def dispatch(self, request, *args, **kwargs):
                    if not request.user.has_perm('paie.delete_article'):
                              raise PermissionDenied

                    return super().dispatch(request, *args, **kwargs)
          


          


        

          
        

