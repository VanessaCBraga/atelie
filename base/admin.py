from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Roupa, Reparo

@admin.register(Roupa)
class RoupaAdmin(admin.ModelAdmin):
    list_display = 'get_imagem','tipo', 'tamanho', 'cor'
    list_filter = 'tipo', 'tamanho','cor'

    def get_imagem(self, obj):
        return mark_safe('<img width="50" src="/{}"></a>'.format(obj.imagem))

    get_imagem.short_description = 'Imagem'

@admin.register(Reparo)
class ReparoAdmin(admin.ModelAdmin):
    list_display = 'descricao', 'data_entrega', 'roupa', 'costureira', 'restaurado'
    list_filter = 'data_entrega', 'costureira'
    exclude = 'data_entrega', 'restaurado'