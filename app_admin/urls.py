from django.urls import path

from .views import *
urlpatterns = [
          
          path('my-articles',user_article,name="my-articles"),
          path('ajouter-article',AddArticle.as_view(),name="ajouter-article"),
          path('update-article/<int:pk>',UpdateArticle.as_view(),name="update-article"),
          path('delete-article/<int:pk>',DeleteArticle.as_view(),name="delete-article"),
          path('article/<int:id_article>', bilan, name="bilan"),
]