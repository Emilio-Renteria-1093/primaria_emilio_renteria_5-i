from django.db import models

# Create your models here.
class Alumno(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="APELLIDO PATERNO")
    Amaterno=models.CharField(max_length=50,verbose_name="APELLIDO MATERNO")
    nombre=models.CharField(max_length=100,verbose_name="NOMBRE (s)")
    fecha_nacimiento=models.CharField(max_length=100,verbose_name="FECHA DE NACIMIENTO",null=False,blank=False)
    fecha_ingreso=models.CharField(max_length=100,verbose_name="FECHA DE INGRESO",null=False,blank=False)
