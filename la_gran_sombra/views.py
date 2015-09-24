#from django.template import RequestContext, loader
from django.shortcuts import render

from .models import Sombra
# Create your views here.
def index(request):
	lista_cadaveres = Sombra.objects.order_by('id')
	#output = ', '.join([p.cadaver for p in lista_cadaveres])
	#template = loader.get_template('la_gran_sombra/index.html')
	context = {'lista_cadaveres': lista_cadaveres}
	return render(request, 'la_gran_sombra/index.html', context)

def cadaver(request):
	return HttpResponse("sarasasarasrasas")