from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.flatpages.models import FlatPage

from roteiros import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from roteiros.models import Roteiros
from roteiros.feeds import UltimasViagens

urlpatterns = patterns('',
    # Examples:
    (r'^$', 'django.views.generic.date_based.archive_index',
      {'queryset': Roteiros.objects.all(), 'date_field': 'publicacao'}),
    # url(r'^syriawings/', include('syriawings.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
      {'feed_dict': {'viagens': UltimasViagens}}),
    (r'^roteiros/(?P<roteiros_id>\d+)/$', 'roteiros.views.roteiros'),
    (r'^contato/$', 'views.contato'),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/js'}),
    (r'^photologue/', include('photologue.urls')),
)

if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
