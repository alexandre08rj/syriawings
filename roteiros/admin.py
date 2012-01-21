from django.contrib import admin
from models import Roteiros

class RoteirosAdmin(admin.ModelAdmin):
    class Media:
        prepopulated_fields = {'slug': ('title',)}
        js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js',)
        

admin.site.register(Roteiros, RoteirosAdmin)
