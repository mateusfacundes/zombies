from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from sobreviventes.models import Sobreviventes, Inventario, Sobreviventesinventario
from sobreviventes.serializers import SobreviventesSerializer, inventarioSerializer, SobreviventesinventarioSerializer
from django.views.decorators.csrf import csrf_exempt

#Sobreviventes

#Metodo para adicionar sobreviventes e inventario através da relação many to many 
@csrf_exempt 
def adicionarSobrevivente(request):
    sobrevivente_data = JSONParser().parse(request)
    sobreviventes_srl = SobreviventesSerializer(data = sobrevivente_data)

    #remoção dos itens dentro da requisição para a validação do novo sobrevivente
    itens = sobrevivente_data.pop('itens')

    #Adição da relação entre itens enviados e sobrevivente recem cadastrado 
    if sobreviventes_srl.is_valid():
        sobreviventes_srl.save()
        sobrevivente = Sobreviventes.objects.last()
        
        for item in itens:
            itemBd = Inventario.objects.get(pk=item['inventario_id'])
            qtd = item['qtd']
            Sobreviventesinventario.objects.create(sobrevivente = sobrevivente, item = itemBd, qtd = qtd)

        return JsonResponse('Sobrevivente adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Sobrevivente', safe=False)

#Mostrar todos sobreviventes
@csrf_exempt 
def mostrarSobreviventes(request):
    sobreviventes = Sobreviventes.objects.all()
    sobreviventes_srl = SobreviventesSerializer(sobreviventes, many=True)
    return JsonResponse(sobreviventes_srl.data, safe=False)

#Mostrar sobrevivente filtrado por ID
@csrf_exempt
def mostrarSobrevivente(request, rid):
	sobrevivente = Sobreviventes.objects.get(sobreviventes_id = rid)
	sobreviventes_srl = SobreviventesSerializer(sobrevivente, many=False)
	return JsonResponse(sobreviventes_srl.data, safe=False)

#Atualizar sobrevivente
@csrf_exempt
def atualizarSobrevivente(request, rid):
    sobrevivente_data = JSONParser().parse(request)
    sobrevivente = Sobreviventes.objects.get(sobreviventes_id = rid)
    sobreviventes_srl = SobreviventesSerializer(sobrevivente, data = sobrevivente_data,  partial=True)
    if sobreviventes_srl.is_valid():
        sobreviventes_srl.save()
        return JsonResponse('Sobrevivente atualizado com sucesso!', safe=False)
    return JsonResponse('Falha ao atualizar Sobrevivente', safe=False)

#Deletar sobrevivente
@csrf_exempt
def deletarSobrevivente(request, rid):
    sobrevivente = Sobreviventes.objects.get(sobreviventes_id = rid)
    sobrevivente.delete()
    return JsonResponse('Sobrevivente deletado com sucesso', safe=False)

#Relatorios
@csrf_exempt 
def relatorioSobreviventes(request):
    qtd_infectados = 0

    qtd_aguas = 0
    qtd_alimentacao = 0
    qtd_medicacao = 0
    qtd_municao = 0

    pontos_perdidos = 0

    sobreviventes = Sobreviventes.objects.all()
    sobreviventesItens_data = Sobreviventesinventario.objects.all()

    for sobrevivente in sobreviventes:
        if sobrevivente.infectato == True:
            qtd_infectados += 1
    for lista in sobreviventesItens_data:
        if lista.item.nome_item == 'Água':
            if lista.sobrevivente.infectato == False:
                qtd_aguas += lista.qtd
            else:
                pontos_perdidos += lista.qtd * 4
        if lista.item.nome_item == 'Alimentação':
            if lista.sobrevivente.infectato == False:
                qtd_alimentacao += lista.qtd
            else:
                pontos_perdidos += lista.qtd * 3
        if lista.item.nome_item == 'Medicação':
            if lista.sobrevivente.infectato == False:
                qtd_medicacao += lista.qtd
            else:
                pontos_perdidos += lista.qtd * 3
        if lista.item.nome_item == 'Munição':
            if lista.sobrevivente.infectato == False:
                qtd_municao += lista.qtd
            else:
                pontos_perdidos += lista.qtd * 3

    porcentagem_infectados = (qtd_infectados*100)/len(sobreviventes)
    media_aguas = qtd_aguas/len(sobreviventes)
    media_alimentacao = qtd_alimentacao/len(sobreviventes)
    media_medicacao = qtd_medicacao/len(sobreviventes)
    media_municao = qtd_municao/len(sobreviventes)

    data = {
        'porcentagem_infectados':porcentagem_infectados,
        'porcentagem_nao_infectados': 100-porcentagem_infectados,
        'media_aguas': media_aguas,
        'media_alimentacao': media_alimentacao,
        'media_medicacao': qtd_medicacao,
        'media_municao': media_municao,
        'pontos_perdidos': pontos_perdidos
    }
    
    return JsonResponse(data, safe=False)


#Itens
#Adicionar itens
@csrf_exempt
def adicionarItens(request):
    item_data = JSONParser().parse(request)
    itens_srl = inventarioSerializer(data = item_data)
    if itens_srl.is_valid():
        itens_srl.save()
        return JsonResponse('item adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado item', safe=False)

#Mostrar itens todos
@csrf_exempt
def mostrarItens(request):
    items = Inventario.objects.all()
    itens_srl = inventarioSerializer(items, many=True)
    return JsonResponse(itens_srl.data, safe=False)

#Mostrar item filtrado por ID
@csrf_exempt
def mostrarItem(request, rid):
	item = Inventario.objects.get(inventario_id = rid)
	itens_srl = inventarioSerializer(item, many=False)
	return JsonResponse(itens_srl.data, safe=False)

#Atualizar item
@csrf_exempt
def atualizarItens(request, rid):
    item_data = JSONParser().parse(request)
    item = Inventario.objects.get(items_id = rid)
    itens_srl = inventarioSerializer(item, data = item_data,  partial=True)
    if itens_srl.is_valid():
        itens_srl.save()
        return JsonResponse("item atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Adicionado item", safe=False)

#Deletar sobrevivente
@csrf_exempt
def deletarItens(request, rid):
    item = Inventario.objects.get(inventario_id = rid)
    item.delete()
    return JsonResponse("item deletado com sucesso", safe=False)

#Items Sobreviventes
#Mostrar relações many to many intes e sobreviventes
@csrf_exempt
def mostrarSobreviventesinventarios(request):
    sobreviventesItens_data = Sobreviventesinventario.objects.all()
    sobreviventesItens_srl = SobreviventesinventarioSerializer(sobreviventesItens_data, many=True)
    return JsonResponse(sobreviventesItens_srl.data, safe=False)
@csrf_exempt
def mostrarSobreviventeinventario(request, rid):
	Sobreviventeinventario = Sobreviventesinventario.objects.filter(sobrevivente_id = rid)
	Sobreviventeinventario_srl = SobreviventesinventarioSerializer(Sobreviventeinventario, many=True)
	return JsonResponse(Sobreviventeinventario_srl.data, safe=False)

