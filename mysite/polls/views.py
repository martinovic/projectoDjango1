from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext
#from django.template import loader
from polls.models import Poll


def index(request):
    '''

    '''
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = RequestContext(request, {'latest_poll_list': latest_poll_list, })
    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context))


def detalle(request, poll_id):
    '''

    '''
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, "polls/detalle.html", {'poll': poll})


def results(request, poll_id):
    '''

    '''
    return HttpResponse("Aca deben ir las respuestas. %s" % poll_id)


def vote(request, poll_id):
    '''

    '''
    return HttpResponse("Aca es donde se vota. %s" % poll_id)