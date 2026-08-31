from django.contrib import admin
from .models import Asset, AssetCategory, Location

admin.site.register(Asset)
admin.site.register(AssetCategory)
admin.site.register(Location)
