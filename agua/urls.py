from django.urls import path, re_path
from agua.views import UsuarioViewSet,  ConsumoViewSet


urlpatterns = [
    path('consumo/', ConsumoViewSet.as_view, name='consumo'),
    path('usuario/', UsuarioViewSet.as_view, name='usuario'),
    re_path(r'usuario/(?P<pk>\d+)/consumo/(?P<dia>\d+)/(?P<mes>\d+)/(?P<ano>\d+)/', ConsumoViewSet.as_view, name='editaconsumo'),

]