from rest_framework import serializers 
from sobreviventes.models import Sobreviventes, Inventario, Sobreviventesinventario

class SobreviventesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobreviventes
        fields = ('sobreviventes_id','nome_sobrevivente', 'idade_sobrevivente', 'sexo_sobrevivente', 'latitude_sobrevivente', 'longitude_sobrevivente', 'infectato', 'flags_infectado')
        depth = 1

class inventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields  = ('inventario_id','nome_item', 'descricao_item')
        depth = 1

class SobreviventesinventarioSerializer(serializers.ModelSerializer):
    sobrevivente = SobreviventesSerializer()
    item = inventarioSerializer()

    class Meta:
            model = Sobreviventesinventario
            fields = ('Sobreviventesinventario_id','sobrevivente','item','qtd')
            depth = 1