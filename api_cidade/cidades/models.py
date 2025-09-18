from django.db import models

# Create your models here.
class Regiao(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True, null=False)
    sigla = models.CharField(max_length=2, unique=True, null=False, verbose_name="Sigla da Região")


class UF(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True, null=False)
    sigla = models.CharField(max_length=2, unique=True, null=False, verbose_name="Sigla da Unidade da Federação")
    regiao = models.ForeignKey(Regiao)

class Municipio(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)
    uf = models.ForeignKey(UF)