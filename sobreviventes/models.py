from pydoc import classname
from django.db import models
from django.db.models import CASCADE

#Sobrevivente Model 
class Sobreviventes(models.Model):
    sobreviventes_id = models.AutoField(primary_key=True)
    nome_sobrevivente = models.CharField(max_length=250)
    idade_sobrevivente = models.IntegerField()
    sexo_sobrevivente = models.CharField(max_length=50)
    latitude_sobrevivente = models.FloatField()
    longitude_sobrevivente = models.FloatField()
    flags_infectado = models.IntegerField(null=True)
    infectato = models.BooleanField()
    Inventario = models.ManyToManyField('Inventario', related_name='itens', through='Sobreviventesinventario')

#Inventario Model
class Inventario(models.Model):
    inventario_id = models.AutoField(primary_key=True)
    nome_item = models.CharField(max_length=250)
    descricao_item = models.CharField(max_length=250)
    
    #Metodo para adicionar valores iniciais em Itens
    def addiniciais():
        agua =  Inventario(nome_item = 'Água', descricao_item = '4 pontos')
        agua.save()
        alimentacao =  Inventario(nome_item = 'Alimentação', descricao_item = '3 pontos')
        alimentacao.save()
        medicacao =  Inventario(nome_item = 'Medicação', descricao_item = '2 pontos')
        medicacao.save()
        municao =  Inventario(nome_item = 'Munição', descricao_item = '1 pontos')
        municao.save()


#Sobrevivente x Inventario Model
class Sobreviventesinventario(models.Model):
    Sobreviventesinventario_id = models.AutoField(primary_key=True)
    sobrevivente = models.ForeignKey(Sobreviventes, on_delete=CASCADE, related_name='sobrevivente')
    item = models.ForeignKey(Inventario, on_delete=CASCADE, related_name='item')
    qtd = models.IntegerField()


