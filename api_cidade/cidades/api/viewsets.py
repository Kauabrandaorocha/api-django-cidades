from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegiaoSerializer, UFSerializer, MunicipioSerializer
from cidades.models import Regiao, UF, Municipio
import requests
import logging

logger = logging.getLogger(__name__)  # Logger para monitoramento

class RegiaoViewSet(viewsets.ModelViewSet):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer

class UFViewSet(viewsets.ModelViewSet):
    queryset = UF.objects.all()
    serializer_class = UFSerializer

    def perform_create(self, serializer):
        uf_sigla = serializer.validated_data['sigla']
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf_sigla}/municipios"
        
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Levanta HTTPError para códigos de erro HTTP

            # Apenas loga a quantidade de municípios retornados (não salva eles aqui)
            data = response.json()
            logger.info(f"API retornou {len(data)} municípios para UF {uf_sigla}")

            # Salva o objeto UF normalmente com os dados do serializer
            serializer.save()

        except requests.exceptions.Timeout:
            logger.warning(f"Timeout na requisição à API do IBGE para UF: {uf_sigla}")
            raise serializers.ValidationError(
                "A requisição demorou demais. Tente novamente mais tarde."
            )

        except requests.exceptions.HTTPError as http_err:
            logger.error(f"Erro HTTP: {http_err}")
            raise serializers.ValidationError(
                "A API do IBGE retornou um erro."
            )

        except Exception as e:
            logger.exception("Erro inesperado ao consultar a API do IBGE.")
            raise serializers.ValidationError(
                "Ocorreu um erro interno ao consultar os municípios."
            )

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
