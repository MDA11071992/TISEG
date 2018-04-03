from django.contrib import admin
from api.models import *

# Register your models here.


class Coordinate (admin.StackedInline):
    model = Coordinates
    ordering = ['route']


@admin.register(Route)
class AdminRoute(admin.ModelAdmin):
    inlines = [Coordinate]
    ordering = ['name']
