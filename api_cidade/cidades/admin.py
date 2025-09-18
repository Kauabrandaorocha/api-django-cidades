from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Regiao, UF, Municipio

# Não será necessário usar o admin.site.register() por conta do @admin.register(Model)

@admin.register(Regiao)
class RegiaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla')  # Exibe essas colunas na lista
    search_fields = ('nome', 'sigla')       # Campo de busca
    ordering = ('id',)

@admin.register(UF)
class UFAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla', 'regiao')  # Exibe essas colunas
    search_fields = ('nome', 'sigla')
    list_filter = ('regiao',)
    ordering = ('id',)

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'uf')     # Exibe essas colunas
    search_fields = ('nome',)
    list_filter = ('uf',)
    ordering = ('id',)

