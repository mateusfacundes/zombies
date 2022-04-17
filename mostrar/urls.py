from django.urls import path
from mostrar import views

urlpatterns = [
    path('', views.sobreviventes),
    path('editar/<str:rid>/', views.editarSobreviventes),

    path('itens/', views.item),
    path('editaritem/<str:rid>/', views.editarItem),

    path('relatorios/', views.relatorios),

]
