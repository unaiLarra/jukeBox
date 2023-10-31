from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Pais, Banda, Estilo

#devuelve el listado de paises
def index_estilos(request):
	estilos = get_list_or_404(Estilo.objects.order_by('nombre'))
	context = {'lista_estilos': estilos}
	return render(request, 'index.html', context)

#devuelve los detalles de un estilo
def show_estilo(request, estilo_id):
	estilo = get_object_or_404(Estilo.objects.get(pk=estilo_id))
	bandas = estilo.banda_set.all()
	context = {'bandas': bandas, 'estilo': estilo}
	return render(request, "estilo.html", context)

#devuelve las bandas de un pais
def index_bandas(request):
	bandas = get_list_or_404(Banda.objects.order_by('nombre'))
	context = {'bandas': bandas}
	return render(request, 'bandas.html', context)

#devuelve los detalles de una banda
def show_banda(request, banda_id):
	banda = get_object_or_404(Banda.objects.get(pk=banda_id))
	estilos = banda.estilos.all()
	context = {'banda': banda, 'estilos': estilos}
	return render(request, 'banda.html', context)

#devuelve los datos de un pais
def show_pais(request, pais_id):
	pais = get_object_or_404(Pais.objects.get(pk=pais_id))
	bandas = pais.banda_set.all()
	context = {'pais': pais, 'bandas': bandas}
	return render(request, 'pais.html', context)

#devuelve las bandas de un pais
def index_paises(request):
	paises = get_list_or_404(Pais.objects.order_by('nombre'))
	context = {'paises': paises}
	return render(request, 'paises.html', context)