from django.contrib import admin
from .models import *

admin.site.register(PadawanProfile)
admin.site.register(CuratorProfile)
admin.site.register(Code)


class Curator(admin.ModelAdmin):
    pass
