from rest_framework import serializers
from cidades.models import Regiao

class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = ['id', 'nome', 'sigla']
        read_only_fields = ['nome', 'sigla']

class UFSerializer(serializers.ModelSerializer):
    regiao = RegiaoSerializer()
    class Meta:
        fields = ['id', 'nome', 'sigla', 'regiao']
        read_only_fields = ['nome', 'sigla', 'regiao']

class MunicipioSerializer(serializers.ModelSerializer):
    uf = UFSerializer()

    class Meta:
        uf = UFSerializer()
        fields = ['id', 'nome', 'uf']
        read_only_fields = ['nome', 'uf']