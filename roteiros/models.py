from datetime import datetime
from django.db import models

class Roteiros(models.Model):
    class Meta:
        ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return '/roteiros/%d/'%self.id
    
    def __unicode__(self):
        return self.titulo

# SIGNALS
from django.db.models import signals
from utils.signals_comuns import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Roteiros)
