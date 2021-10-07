
from video.models import Video
from django.shortcuts import render
from django.db.models import query
from django.views.generic.edit import CreateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from paie.forms import VideoForm



def indax(request):
          title='Liste des videos'
          list_videos=Video.objects.all()
          context={'list_videos':list_videos,'title':title}
          return render(request,'indax.html',context)


@login_required

def user_video(request):
          has_perm= False
          if request.user.has_perm("project.delete_article"):
                    has_perm= True
          list_articles= Video.objects.filter(user=request.user)
          return render(request,'my-video.html',{'list_videos':list_articles,"has_perm":has_perm})
def detial(request, id_video):
          titre='Detail des videos'
          video=Video.objects.get(id=id_video)  
          category=video.category  
          videos_en_relation=Video.objects.filter(category=category)[:5]
          title= 'Videos en relation'
          return render(request,'detial.html', {'video':video,"aer":videos_en_relation,'titre':titre,'title':title})

def sarch(request):
          query=request.GET["video"]
          list_videos = Video.objects.filter(caption__contains=query)           
          return render(request, 'sarch.html',{"list_videos": list_videos})



class AddVideo(CreateView):
          model=Video
          form_class=VideoForm
          template_name='ajouter-video.html'
          success_url="/video/indax/"


class DeleteVideo(DeleteView):
          model = Video        
          success_url ="/video/indax/"

          def dispatch(self, request, *args, **kwargs):
                    if not request.user.has_perm('video.delete_video'):
                              raise PermissionDenied

                    return super().dispatch(request, *args, **kwargs) 
    

