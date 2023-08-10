from django.contrib import admin
from django.urls import path, include
from agua.views import UsuarioViewSet, ConsumoViewSet,   HistoricoPorDia, HistoricoPorDiasPassados
from rest_framework import routers


router = routers.DefaultRouter()
router.register('consumo', viewset=ConsumoViewSet, basename='consumo')
router.register('usuario',viewset=UsuarioViewSet, basename='usuario')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path('usuario/<int:pk>/consumo/', ConsumoViewSet.as_view({'get':'list'}), name='consulta-consumo'),
    path('usuario/<int:pk>/consumo/<int:dia>/<int:mes>/<int:ano>/', ConsumoViewSet.as_view({'get':'list'}), name='consulta-consumo-dia'),
    path('usuario/<int:pk>/consumo/historico/', HistoricoPorDiasPassados.as_view(), name='historico-consumo-dias'),
    path('usuario/<int:pk>/consumo/historico/<int:dia>/<int:mes>/<int:ano>/', HistoricoPorDia.as_view(), name='historico-consumo-dia'),
]