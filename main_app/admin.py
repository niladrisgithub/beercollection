from django.contrib import admin

# Register your models here.
from .models import Beer, Drinking, Hop, Venue

admin.site.register(Beer)
admin.site.register(Hop)
admin.site.register(Drinking)
admin.site.register(Venue)