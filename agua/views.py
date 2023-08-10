from rest_framework import viewsets, generics
from agua.models import Usuario, Consumo
from agua.serializer import ConsumoSerializer, UsuarioSerializer, HistoricoPorDiaSerializer
from django.db.models import Sum
from datetime import date, timedelta

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class ConsumoViewSet(viewsets.ModelViewSet):
    serializer_class = ConsumoSerializer
    queryset = Consumo.objects.all()
    search_fields = ['usuario_id', 'data']
    
    def filter_queryset(self, queryset):
        try:
            pk = self.kwargs['pk']
            try:
                dia, mes, ano =  self.kwargs['dia'], self.kwargs['mes'], self.kwargs['ano']
                data = f'{ano}-{mes}-{dia}'
            except:
                data = date.today()
        except:
            return super().filter_queryset(queryset)
        queryset = queryset.filter(usuario_id=pk, data=data)
        return queryset
        



    
class HistoricoPorDia(generics.ListAPIView):
    serializer_class = HistoricoPorDiaSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['pk']
        try:
            ano, mes, dia = self.kwargs['ano'], self.kwargs['mes'], self.kwargs['dia']
            data = f'{ano}-{mes}-{dia}'
        except:
            data = date.today()
        queryset = Consumo.objects.filter(usuario_id=usuario_id, data=data)
        data = queryset.first().data
        meta = queryset.first().meta_diaria 
        usuario_id = queryset.first().usuario.pk
        consumo_total = queryset.aggregate(consumo_total=Sum('consumo'))['consumo_total']
        percentual_consumido = consumo_total / meta * 100
        meta_consumida = consumo_total
        objeto_consumo = Consumo(consumo=consumo_total, usuario_id=usuario_id, data=data, 
                                 meta_diaria=meta, percentual_consumido= percentual_consumido, meta_consumida=meta_consumida)
        return [objeto_consumo]
    
    

class HistoricoPorDiasPassados(generics.ListAPIView):
    serializer_class = HistoricoPorDiaSerializer
    
    def get_queryset(self):
        usuario_id = self.kwargs['pk']
        datas = [date.today() - timedelta(days=i) for i in range(3)]
        queryset = Consumo.objects.filter(usuario_id=usuario_id, data__in=datas)

        objetos_consumo = []
        for data in datas:
            consumo_total = queryset.filter(data=data).aggregate(consumo_total=Sum('consumo'))['consumo_total']
            meta = queryset.first().meta_diaria
            try:
                percentual_consumido = consumo_total / meta * 100
            except:
                percentual_consumido = 0

            objeto_consumo = Consumo(consumo=consumo_total, usuario_id=usuario_id, data=data, meta_diaria=meta, percentual_consumido=percentual_consumido, meta_consumida=consumo_total)
            objetos_consumo.append(objeto_consumo)

        return objetos_consumo



