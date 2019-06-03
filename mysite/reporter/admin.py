from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from reporter.models import Incidences

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
	 list_display =('name', 'location')

admin.site.register(Incidences,IncidencesAdmin)