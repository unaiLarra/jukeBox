from django.contrib import admin
from .models import Banda, Pais, Estilo

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_pais', 'get_estilos', 'descripcion', 'imagen')
    list_filter = ('pais__nombre', 'estilos__nombre')
    search_fields = ('nombre', 'pais__nombre', 'estilos__nombre')
    list_per_page = 20  

    actions = ['marcar_como_activa']

    def marcar_como_activa(self, request, queryset):
        queryset.update(estado='activo')
    marcar_como_activa.short_description = "Marcar como activa"


    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'pais', 'estilos')
        }),
        ('Configuración Avanzada', {
            'classes': ('collapse',),
            'fields': ('imagen',),
        }),
    )

    def get_pais(self, obj):
        return obj.pais.nombre if obj.pais else ''
    get_pais.short_description = 'País'

    def get_estilos(self, obj):
        return ", ".join([estilo.nombre for estilo in obj.estilos.all()])
    get_estilos.short_description = 'Estilos'


    class Media:
        css = {
            'all': ('appJukeBox/static/css/custom_admin_styles.css',)
        }

admin.site.register(Banda, BandaAdmin)

class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

    
    actions = ['marcar_como_pais_popular']

    def marcar_como_pais_popular(self, request, queryset):
        queryset.update(popular=True)
    marcar_como_pais_popular.short_description = "Marcar como país popular"

admin.site.register(Pais, PaisAdmin)

class EstiloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

    
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion'),
        }),
    )

admin.site.register(Estilo, EstiloAdmin)