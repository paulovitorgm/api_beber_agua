from django.contrib import admin
from django.urls import path, include
from agua.views import UsuarioViewSet, ConsumoViewSet, ConsultaConsumo, ConsultaConsumoDia, HistoricoPorDia
from rest_framework import routers


router = routers.DefaultRouter()
router.register('usuario', UsuarioViewSet, 'usuario')
router.register('consumo/<int:pk>/<int:agua>', ConsumoViewSet, 'consumo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('usuario/<int:pk>/consumo/', ConsultaConsumo.as_view()),
    path('usuario/<int:pk>/consumo/<int:dia>-<int:mes>-<int:ano>/', ConsultaConsumoDia.as_view()),
    path('usuario/<int:pk>/consumo/<int:dia>-<int:mes>-<int:ano>/historico/', HistoricoPorDia.as_view()),
    
]
