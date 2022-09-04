from rest_framework import serializers

from .models import *


class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields = '__all__'
    
    def to_representation(self,instance):
            representation = super().to_representation(instance)
            representation['imagen_noticias'] = instance.imagen_noticias.url
            return representation



class TestimonioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonio
        fields = '__all__'
    
    def to_representation(self,instance):
            representation = super().to_representation(instance)
            representation['foto'] = instance.foto.url
            return representation



    # def create(self,validated_data):
    #     noticias=Noticias(
    #         imagen_noticias=validated_data['imagen_noticias'],
    #         descripcion=validated_data['descripcion'],
    #         video=validated_data['video'],
    #         informacion=validated_data['informacion']
    #     )

