from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from .forms import SombraForm, TimerForm
from .models import Sombra


def timer(request):
    if request.method == "POST":
        form = TimerForm(request.POST)
        if form.is_valid():
            return redirect(reverse('la_gran_sombra:create'))
    else:
        form = TimerForm(initial={'minutes': 0})
    context = {}
    context['form'] = form
    return render(request, 'la_gran_sombra/timer.html', context)


def form(request):
    if request.method == "POST":
        form = SombraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('la_gran_sombra:thanks'))
    else:
        form = SombraForm()
    context = {}
    context['form'] = form
    return render(request, 'la_gran_sombra/form.html', context)


def list(request):
    lista_cadaveres = Sombra.objects.order_by('id')
    # output = ', '.join([p.cadaver for p in lista_cadaveres])
    context = {}
    context['lista_cadaveres'] = lista_cadaveres
    return render(request, 'la_gran_sombra/list.html', context)

def thanks(request):
    return render(request, 'la_gran_sombra/thanks.html')