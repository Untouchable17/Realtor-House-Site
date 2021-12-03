from django.contrib import admin

from src.realtor_app import models


@admin.register(models.Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "joined_at")
    list_display_links = ("id", "email")
    search_fields = ("name",)

