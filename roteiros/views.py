from django.shortcuts import render_to_response

from models import Roteiros


def roteiros(request, roteiros_id):
    roteiros = Roteiros.objects.get(id=roteiros_id)
    return render_to_response('roteiros/viagem.html', locals())
