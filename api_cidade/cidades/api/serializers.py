from rest_framework import serializers
from cidades.models import Regiao, UF, Municipio

class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = ['id', 'nome', 'sigla']

class UFSerializer(serializers.ModelSerializer):
    regiao = RegiaoSerializer(read_only=True)  # Serializa a região completa para leitura
    regiao_id = serializers.PrimaryKeyRelatedField(  # Permite passar o ID da região para escrita (POST/PUT)
        queryset=Regiao.objects.all(),  # Queryset para validação do ID da região
        source='regiao',  # Diz que esse campo escreve no atributo 'regiao' do modelo
        write_only=True  # Campo write-only, não aparece na leitura, só na escrita
    )

    class Meta:
        model = UF
        fields = ['id', 'nome', 'sigla', 'regiao', 'regiao_id']  # Inclui ambos os campos: leitura e escrita

class MunicipioSerializer(serializers.ModelSerializer):
    uf = UFSerializer(read_only=True)  # Serializa a UF completa para leitura
    uf_id = serializers.PrimaryKeyRelatedField(  # Permite passar o ID da UF para escrita (POST/PUT)
        queryset=UF.objects.all(),  # Queryset para validação do ID da UF
        source='uf',  # Diz que esse campo escreve no atributo 'uf' do modelo
        write_only=True  # Campo write-only, não aparece na leitura, só na escrita
    )

    class Meta:
        model = Municipio
        fields = ['id', 'nome', 'uf', 'uf_id']  # Inclui ambos os campos: leitura e escrita
