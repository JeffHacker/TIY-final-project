from django.contrib import admin
from .models import UploadedData, ClosedTrade, Graph

# Register your models here.

admin.site.register(UploadedData)
admin.site.register(ClosedTrade)
admin.site.register(Graph)
