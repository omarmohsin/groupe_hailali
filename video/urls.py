from django.urls import path
from video.views  import *
urlpatterns = [
          path('indax/',indax,name='indax'),
          path('my-videos',user_video,name="my-videos"),
          path('video/<int:id_video>', detial, name="detial"), 
          path('ajouter-video',AddVideo.as_view(),name="ajouter-video"),
          path('delete-video/<int:pk>',DeleteVideo.as_view(),name="delete-video"),
                   
          
          

          

]