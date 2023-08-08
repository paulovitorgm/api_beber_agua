from django.contrib import admin
from django.urls import path, include
from agua.views import UsuarioViewSet, ConsumoViewSet, ConsultaConsumo, ConsultaConsumoDia, HistoricoPorDia
from rest_framework import routers


router = routers.DefaultRouter()
router.register('consumo', viewset=ConsumoViewSet, basename='consumo')
router.register('usuario',viewset=UsuarioViewSet, basename='usuario')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path('usuario/<int:pk>/consumo/', ConsultaConsumo.as_view(), name='consulta-consumo'),
    path('usuario/<int:pk>/consumo/<int:dia>/<int:mes>/<int:ano>/', ConsultaConsumoDia.as_view(), name='consulta-consumo-dia'),
    path('usuario/<int:pk>/consumo/historico/<int:dia>/<int:mes>/<int:ano>/', HistoricoPorDia.as_view(), name='historico-consumo-dia'),
]