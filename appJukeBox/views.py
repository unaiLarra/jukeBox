from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from .models import Pais, Banda, Estilo
from .forms import BandaForm

#devuelve el listado de paises
def index_pais_banda(request):
	listabandas = Banda.objects.raw('SELECT * FROM( SELECT * FROM appJukeBox_Banda ORDER BY nombre DESC) GROUP BY pais_id')
	context = {'lista_banda': listabandas}
	return render(request, 'index.html', context)

#devuelve los detalles de un estilo
def show_estilo(request, estilo_id):
	estilo = get_object_or_404(Estilo, pk=estilo_id)
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
	banda = get_object_or_404(Banda, pk=banda_id)
	estilos = banda.estilos.all()
	context = {'banda': banda, 'estilos': estilos}
	return render(request, 'banda.html', context)

#devuelve los datos de un pais
def show_pais(request, pais_id):
	pais = get_object_or_404(Pais, pk=pais_id)
	bandas = pais.banda_set.all()
	context = {'pais': pais, 'bandas': bandas}
	return render(request, 'pais.html', context)

#devuelve la lista de paises
def index_paises(request):
	paises = get_list_or_404(Pais.objects.order_by('nombre'))
	context = {'paises': paises}
	return render(request, 'paises.html', context)

#devuelve las bandas de un pais
def index_estilos(request):
	estilos = get_list_or_404(Estilo.objects.order_by('nombre'))
	context = {'estilos': estilos}
	return render(request, 'estilos.html', context)

def upload_banda(request):
	submitted = False
	if request.method == "POST":
		form = BandaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			print("Should be saved!")
			return HttpResponseRedirect("formulario?submitted=True")
	
	else:
		form = BandaForm()
		if "submitted" in request.GET:
			submitted = True

	context = {'form': form, 'submitted':submitted}
	return render(request, 'formulario.html', context)