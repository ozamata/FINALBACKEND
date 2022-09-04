from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.


class Noticias(models.Model):
    noticias_id=models.AutoField(primary_key=True)
    imagen_noticias= CloudinaryField('image',default='')
    descripcion = models.TextField()
    video = models.TextField()
    informacion = models.TextField()


    class Meta:
        db_table = 'tbl_noticias'

    def __str__(self):
        return self.descripcion


class Testimonio(models.Model):
    testimonio_id=models.AutoField(primary_key=True)
    foto= CloudinaryField('image',default='')
    nombre = models.TextField()
    descripcion = models.TextField()

    class Meta:
        db_table = 'tbl_testimonio'

    def __str__(self):
        return self.nombre