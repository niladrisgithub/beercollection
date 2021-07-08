from django.contrib import admin

# Register your models here.
from .models import Beer, Hop, Drinking

admin.site.register(Beer)
admin.site.register(Hop)
admin.site.register(Drinking)