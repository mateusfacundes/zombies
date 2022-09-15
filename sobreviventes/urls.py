from django.urls import path
from sobreviventes import views

urlpatterns = [
    path('', views.mostrarSobreviventes),
    path('sobrevivente/<str:rid>/', views.mostrarSobrevivente),
	path('adicionarsobrevivente/', views.adicionarSobrevivente),
    path('atualizarsobrevivente/<str:rid>/', views.atualizarSobrevivente),
	path('deletarsobrevivente/<str:rid>/', views.deletarSobrevivente),
    path('relatorio/', views.relatorioSobreviventes),
    
    path('itens', views.mostrarItens),
    path('itens/<str:rid>/', views.mostrarItem),
	path('adicionaritens/', views.adicionarItens),
    path('atualizaritens/<str:rid>/', views.atualizarItens),
	path('deletaritens/<str:rid>/', views.deletarItens),

    path('sobreviventesitens/' , views.mostrarSobreviventesinventarios),
    path('sobreviventesitens/<str:rid>/' , views.mostrarSobreviventeinventario),
]
