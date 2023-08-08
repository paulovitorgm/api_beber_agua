from rest_framework import viewsets, generics
from agua.models import Usuario, Consumo
from agua.serializer import ConsumoSerializer, UsuarioSerializer, ResultadoDoDiaSerializer, HistoricoPorDiaSerializer
from django.db.models import Sum



class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class ConsumoViewSet(viewsets.ModelViewSet):
    serializer_class = ConsumoSerializer
    queryset = Consumo.objects.all()


class ConsultaConsumo(generics.ListAPIView):
    serializer_class = ResultadoDoDiaSerializer
    def get_queryset(self):
        queryset = Consumo.objects.filter(usuario_id=self.kwargs['pk'])    
        return queryset


class ConsultaConsumoDia(generics.ListAPIView):
    serializer_class = ResultadoDoDiaSerializer
    def get_queryset(self):
        queryset = Consumo.objects.filter(usuario_id=self.kwargs['pk'], data__year=self.kwargs['ano'], 
                                          data__month=self.kwargs['mes'], data__day=self.kwargs['dia'])
        return queryset

    
class HistoricoPorDia(generics.ListAPIView):
    serializer_class = HistoricoPorDiaSerializer

    def get_queryset(self):
        queryset = Consumo.objects.filter(usuario_id=self.kwargs['pk'], data__year=self.kwargs['ano'], data__month=self.kwargs['mes'], data__day=self.kwargs['dia'])
        meta = queryset.first().meta_diaria
        data = queryset.first().data
        usuario_id = queryset.first().usuario.pk
        consumo_total = queryset.aggregate(consumo_total=Sum('consumo'))['consumo_total']
        percentual_consumido = consumo_total / meta * 100
        meta_consumida = consumo_total
        objeto_consumo = Consumo(consumo=consumo_total, usuario_id=usuario_id, data=data, meta_diaria=meta, percentual_consumido= percentual_consumido, meta_consumida=meta_consumida)
        return [objeto_consumo]
    




    


    