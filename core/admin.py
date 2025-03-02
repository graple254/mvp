from django.contrib import admin
from .models import *


class VisitorAdmin(admin.ModelAdmin):
    list_display = ("visit_date", "location")


admin.site.register(Visitor, VisitorAdmin)