from django.contrib.syndication.feeds import Feed

from models import Roteiros

class UltimasViagens(Feed):
    title = 'Ultimos roteiros de viagens da Syria Wings'
    link = '/'

    def items(self):
        return Roteiros.objects.all()

