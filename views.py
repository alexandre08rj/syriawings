from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms

class FormContato(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensagem = forms.Field(widget=forms.Textarea)

def contato(request):
    form = FormContato()
    return render_to_response(
        'contato.html',
        locals(),
        context_instance=RequestContext(request),
        )