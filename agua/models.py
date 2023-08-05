from django.db import models



class Usuario(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=30)
    peso = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return self.nome
    

class Consumo(models.Model):
    copo = ((250,250),(350,350),(500,500))
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    meta_diaria = models.IntegerField(editable=False)
    meta_consumida = models.IntegerField(editable=False, default=0)
    consumo = models.IntegerField(blank=False, null=False, choices=copo)
    data = models.DateField(blank=False, null=False, editable=False)
    
    def __str__(self):
        return self.usuario.nome
    



