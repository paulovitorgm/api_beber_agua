from rest_framework import serializers
from agua.models import Consumo, Usuario
from datetime import date


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class ConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        exclude = ['id',]

    def create(self, validated_data):
        usuario = validated_data['usuario']
        peso = usuario.peso
        meta_diaria = peso * 35
        validated_data['meta_diaria'] = meta_diaria
        validated_data['data'] = date.today()
        return super().create(validated_data)
    
    


class ResultadoDoDiaSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.nome')
    class Meta:
        model = Consumo
        exclude = ['id']
        
    

class HistoricoPorDiaSerializer(serializers.ModelSerializer):  
    usuario = serializers.ReadOnlyField(source='usuario.nome')
    bateu_a_meta = serializers.SerializerMethodField()
    class Meta:
        model = Consumo
        exclude = ['id', 'consumo']

    def get_bateu_a_meta(self, obj):
        m1= obj.meta_consumida >= obj.meta_diaria
        return m1