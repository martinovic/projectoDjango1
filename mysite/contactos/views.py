#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# from django.http import HttpResponse

from django.template import RequestContext
from contactos.models import Contactos
from django.core.context_processors import csrf


def index(request):
    '''

    '''

    lista_contactos = Contactos.objects.order_by('-razonNombreApellido'
            ).all()
    context = RequestContext(request,
                             {'lista_contactos': lista_contactos})
    return render(request, 'contactos/index.html', context)


def append_contacto(request):
    '''Append to agenda'''

    c = {}
    c.update(csrf(request))
    context = {}
    if request.method == 'POST':
        if request.POST['id'] != 'none':
            datos = Contactos.objects.get(pk=int(request.POST['id']))
            context = {'posts': datos}
    return render(request, 'contactos/append_contactos.html', context)


def save_contactos(request):
    '''Graba los datos'''

    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        razonNombreApellido = request.POST['razonNombreApellido']
        calle = request.POST['calle']
        numero = request.POST['numero']
        piso = request.POST['piso']
        ciudad = request.POST['ciudad']
        provincia = request.POST['provincia']
        pais = request.POST['pais']
        telefono1 = request.POST['telefono1']
        telefono2 = request.POST['telefono2']
        telefono3 = request.POST['telefono3']
        telefono4 = request.POST['telefono4']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        email3 = request.POST['email3']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        googleplus = request.POST['googleplus']
        webpage = request.POST['webpage']
        tipoEntrada = request.POST['tipoEntrada']
        entrega = request.POST['entrega']
        productos = request.POST['productos']
        pago = request.POST['pago']
        cuit = request.POST['cuit']
        cbu = request.POST['cbu']
        banco = request.POST['banco']
        horario = request.POST['horario']
        observaciones = request.POST['observaciones']
        transportes = request.POST['transportes']
        if request.POST['id'] != '':
            cs = Contactos.objects.get(pk=request.POST['id'])
            cs.razonNombreApellido = razonNombreApellido
            cs.calle = calle
            cs.numero = numero
            cs.piso = piso
            cs.ciudad = ciudad
            cs.provincia = provincia
            cs.pais = pais
            cs.telefono1 = telefono1
            cs.telefono2 = telefono2
            cs.telefono3 = telefono3
            cs.telefono4 = telefono4
            cs.email1 = email1
            cs.email2 = email2
            cs.email3 = email3
            cs.facebook = request.POST['facebook']
            cs.twitter = request.POST['twitter']
            cs.googleplus = request.POST['googleplus']
            cs.webpage = request.POST['webpage']
            cs.tipoEntrada = tipoEntrada
            cs.entrega = entrega
            cs.productos = productos
            cs.pago = pago
            cs.cuit = cuit
            cs.banco = banco
            cs.cbu = cbu
            cs.horario = horario
            cs.observaciones = observaciones
            cs.transportes = transportes
        else:
            cs = Contactos(
                razonNombreApellido=razonNombreApellido,
                calle=calle,
                numero=numero,
                piso=piso,
                ciudad=ciudad,
                provincia=provincia,
                pais=pais,
                telefono1=telefono1,
                telefono2=telefono2,
                telefono3=telefono3,
                telefono4=telefono4,
                email1=email1,
                email2=email2,
                email3=email3,
                facebook=facebook,
                twitter=twitter,
                googleplus=googleplus,
                webpage=webpage,
                tipoEntrada=tipoEntrada,
                productos=productos,
                entrega=entrega,
                pago=pago,
                cuit=cuit,
                banco=banco,
                transportes=transportes,
                cbu=cbu,
                horario=horario,
                observaciones=observaciones,
                )
        try:
            cs.save()
            return render(request, 'contactos/save_contactos.html')
        except:
            return render(request, 'contactos/failsave_contactos.html')


def delete_contacto(request):
    '''Borrado de datos'''

    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        try:
            Contactos.objects.get(pk=request.POST['id']).delete()
            context = {'estado': 'ok',
                       'message': 'Se ha borrado el registro.'}
        except:
            context = {'estado': 'fail',
                       'message': 'No se pudo borrar el archivo'}

        return render(request, 'contactos/delete_contactos.html',
                      context)


def search_contacto(request):
    '''Busqueda de datos'''

    c = {}
    c.update(csrf(request))
    try:
        datos = get_object_or_404(Contactos,
                                  razonNombreApellido__contains=request.POST['s'
                                  ])
        context = {'posts': datos}
    except:
        context = {'error_message': 'Dato no encontrado'}

    return render(request, 'contactos/search_contactos.html', context)


