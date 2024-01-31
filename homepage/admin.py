from django.contrib import admin
from .models import ThreeDPrintOrder, LaserEngravingOrder

# Register your models here.
admin.site.register(ThreeDPrintOrder)
admin.site.register(LaserEngravingOrder)
