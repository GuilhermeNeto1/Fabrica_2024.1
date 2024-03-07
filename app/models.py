from django.db import models

# Create your models here.
class ViaCep(models.Model):
    cep = models.CharField(verbose_name="cep",max_length=255)
    logradouro = models.CharField(verbose_name="logradouro",max_length=255,blank=True,null=True)
    complemento = models.CharField(verbose_name="complemento",max_length=255,blank=True,null=True)
    bairro= models.CharField(verbose_name="bairro",max_length=255,blank=True,null=True)
    localidade= models.CharField(verbose_name="localidade",max_length=255,blank=True,null=True)
    uf= models.CharField(verbose_name="uf",max_length=255,blank=True,null=True)

    