from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_on',
                    'created_by']


admin.site.register(Team, TeamAdmin)
