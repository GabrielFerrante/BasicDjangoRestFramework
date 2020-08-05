from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        #Parâmetros extras
        #Email não será apresentado, somente exigido quando for escrita
        extra_kwargs = {
            'email': {'write_only':True}
        }
        model = Avaliacao
        #Dados que serão mostrados
        fields = [
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        ]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        ]