from django.contrib import admin
from .models import UploadedData, ClosedTrades

# Register your models here.

admin.site.register(UploadedData)
admin.site.register(ClosedTrades)
