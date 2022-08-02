from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload


# Create your models here.

class MasDatosUsuario(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)



