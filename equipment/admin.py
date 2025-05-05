from django.contrib import admin
from .models import Equipment, Rental, MaintenanceLog

admin.site.register(Equipment)
admin.site.register(Rental)
admin.site.register(MaintenanceLog)
