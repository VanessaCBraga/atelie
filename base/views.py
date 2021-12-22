from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from base.forms import RegistrarReparoForm


def registrar_reparo(request):
    form = RegistrarReparoForm(data=request.POST or None)
    if form.is_valid():
        form.processar()
        messages.success(request, 'Reparo registrada com sucesso.')
        return HttpResponseRedirect('/admin/')
    return render(request, 'registrar_reparo.html', dict(form=form))