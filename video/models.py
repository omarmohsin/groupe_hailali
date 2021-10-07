

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
              name= models.CharField(max_length=120)

              def __str__(self) :
                        return self.name


class Video(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          caption=models.CharField(max_length= 100)
          category = models.ForeignKey(
              Category, on_delete=models.CASCADE, null=True, blank=True)
          description=models.TextField()
          video=models.FileField(upload_to="video/%y")
          created_at = models.DateTimeField(auto_now_add=True)
          update_at = models.DateTimeField(auto_now=True)
          times = models.DateTimeField(auto_now_add=True, auto_now=False)
          def __str__(self) :
                        return self.caption




