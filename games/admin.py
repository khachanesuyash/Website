from django.contrib import admin
from .models import Game
from import_export.admin import ImportExportModelAdmin



class ViewAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Game, ViewAdmin)