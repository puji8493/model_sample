from django.contrib import admin
from .models import Countries, Authors, Sects,Works

admin.site.register(Countries)
admin.site.register(Authors)
admin.site.register(Sects)
admin.site.register(Works)
