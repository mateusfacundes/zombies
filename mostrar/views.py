from django.shortcuts import render
from sobreviventes.models import Inventario, Sobreviventes, Sobreviventesinventario
from django.core import serializers

# sobreviventes view com intens cadastrados para campo formulario 
def sobreviventes(request):
    items = Inventario.objects.all()
    context = {
        'itens': items
    }
    return render(request, 'mostrar/sobrevivente.html', context)

# Editar sobreviventes view
def editarSobreviventes(request, rid):
    return render(request, 'mostrar/editar_sobrevivente.html', {'id': rid})

#Item view
def item(request):
    if Inventario.objects.filter(nome_item="Água"):
        print('adicionado')
    else:
        Inventario.addiniciais()

    return render(request, 'mostrar/item.html')

# Editar Item view
def editarItem(request, rid):
    return render(request, 'mostrar/editar_itens.html', {'id': rid})

# Relatorio view
def relatorios(request):
    #envio de todas informações para geração do relatorio
    itens = serializers.serialize("json",Inventario.objects.all())
    sobreviventes = serializers.serialize("json", Sobreviventes.objects.all())
    sobreviventeitems = serializers.serialize("json", Sobreviventesinventario.objects.all())

    print(itens[1])


    context = {
        'itens': itens,
        'sobreviventes':  sobreviventes,
        'sobreviventeitems': sobreviventeitems


    }
    return render(request, 'mostrar/relatorios.html', context)