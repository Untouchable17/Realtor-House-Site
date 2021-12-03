from django.contrib import admin
from django.utils.safestring import mark_safe

from src.strainer import models


admin.site.register(models.HomeTypeCategory)
admin.site.register(models.SaleTypeCategory)

@admin.register(models.House)
class StrainerItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "is_published",)
    list_display_links = ("id", "title")
    search_fields = ("title", "description", "zipcode", "price", "state", "address")
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ("is_published", )


@admin.register(models.HomeImages)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("house", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} style="width:50px;height:50px;object-fit:cover;">')

    get_image.short_description = "Изображение"