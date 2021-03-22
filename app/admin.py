from django.contrib import admin

from app.models import Picture, PictureHistory


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['login', 'created_date', ]


@admin.register(PictureHistory)
class PictureHistoryAdmin(admin.ModelAdmin):
    pass
