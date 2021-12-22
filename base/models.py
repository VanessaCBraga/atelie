from django.contrib.auth.models import User, Permission
from django.db import models
from datetime import date

# Create your models here.
class Roupa(models.Model):
    tipo = models.CharField(verbose_name='Tipo', choices=[['VESTIDO', 'Vestido'], ['CALÇA', 'Calça'], ['BLUSA', 'Blusa'], ['SHORT', 'Short']], max_length=50)
    tamanho = models.CharField(verbose_name='Tamanho', max_length=50)
    cor = models.CharField(verbose_name='Cor', max_length=50)
    imagem = models.ImageField(verbose_name='Imagem', upload_to='roupas', null=True)

    class Meta:
        verbose_name = 'Roupa'
        verbose_name_plural = 'Roupas'

    def __str__(self):
        return '{} - {} ({}|{})'.format(self.id, self.tipo, self.tamanho, self.cor)

class Reparo(models.Model):
    descricao = models.TextField(verbose_name='Descrição', max_length=150)
    data_entrega = models.DateField(verbose_name='Data de Entrega', null=True, blank=True)
    roupa = models.ForeignKey(Roupa, verbose_name='Roupa', on_delete=models.CASCADE)
    costureira = models.ForeignKey(User, verbose_name='Costureira', on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, verbose_name='Cliente', on_delete=models.CASCADE, related_name='reparo_solicitado', default= 1)
    restaurado = models.BooleanField(verbose_name='Restaurado', default=False)

    class Meta:
        verbose_name = 'Reparo'
        verbose_name_plural = 'Reparos'

    def __str__(self):
        return '{} - {} ({})'.format(self.descricao, self.roupa.tipo, self.costureira)