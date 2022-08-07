from dataclasses import field
from rest_framework import serializers
from .models import Video, Categoria
from .validate import emptyValue
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
    def validate(self, data):
        if emptyValue(data['titulo']):
            raise serializers.ValidationError({'titulo': 'Preencha o campo de titulo'})
        if emptyValue(data['url']):
            raise serializers.ValidationError({'url': 'Preencha a URL'})
        return data
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    def validate(self, data):
        if emptyValue(data['titulo']):
            raise serializers.ValidationError({'titulo': 'O titulo é obrigatório'})
        if not emptyValue(data['cor']):
            if len(data['cor']) > 9 or '#' not in data['cor'] or ' ' in data['cor']:
                raise serializers.ValidationError({'cor': 'A cor deve seguir o modelo: #123456'})
        else:
            raise serializers.ValidationError({'cor': 'A cor é obrigatória'})
        return data

class VideosInCategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['titulo', 'descricao']

class FreeVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'categoria']
    