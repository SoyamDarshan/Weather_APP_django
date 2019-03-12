from django.contrib import admin
from .models import RainfallData, TmaxData, TminData
# Register your models here.

admin.site.register(RainfallData)
admin.site.register(TminData)
admin.site.register(TmaxData)
