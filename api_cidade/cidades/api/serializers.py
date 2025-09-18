from rest_framework import serializers
from cidades.models import Regiao, UF, Municipio

class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = ['id', 'nome', 'sigla']

class UFSerializer(serializers.ModelSerializer):
    regiao = RegiaoSerializer(read_only=True)  # exibe os dados da região
    regiao_id = serializers.PrimaryKeyRelatedField(
        queryset=Regiao.objects.all(),
        source='regiao',
        write_only=True  # apenas para entrada (POST/PUT)
    )

    class Meta:
        model = UF
        fields = ['id', 'sigla', 'regiao', 'regiao_id'] 

class MunicipioSerializer(serializers.ModelSerializer):
    uf = serializers.SlugRelatedField(read_only=True, slug_field='sigla')  # ✅ mostra só a sigla
    uf_id = serializers.PrimaryKeyRelatedField(
        queryset=UF.objects.all(),
        source='uf',
        write_only=True
    )

    class Meta:
        model = Municipio
        fields = ['id', 'nome', 'uf', 'uf_id']

