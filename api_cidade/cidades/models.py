from django.db import models

# Create your models here.
class Regiao(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True, null=False)
    sigla = models.CharField(max_length=2, unique=True, null=False, verbose_name="Sigla da Região")

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


class UF(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True, null=False)
    sigla = models.CharField(max_length=2, unique=True, null=False, verbose_name="Sigla da Unidade da Federação")
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"

class Municipio(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.uf.sigla}"