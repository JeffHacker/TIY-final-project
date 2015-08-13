from django.contrib import admin
from .models import UploadedData, ClosedTrade, Graph, TradeNotes

# Register your models here.

admin.site.register(UploadedData)
admin.site.register(ClosedTrade)
admin.site.register(Graph)
admin.site.register(TradeNotes)

