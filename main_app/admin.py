from django.contrib import admin

# Register your models here.
from .models import Beer, Hop

admin.site.register(Beer)
admin.site.register(Hop)