from rest_framework import serializers
from cidades.models import Regiao

class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = ['id', 'nome', 'sigla']
        ready_only_fields = ['nome', 'sigla']

class UFSerializer(serializers.ModelSerializer):
    class Meta:
        regiao = RegiaoSerializer()
        fields = ['id', 'nome', 'sigla', 'regiao']
        ready_only_fields = ['nome', 'sigla', 'regiao']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        uf = UFSerializer()
        fields = ['id', 'nome', 'uf']
        ready_only_fields = ['nome', 'uf']