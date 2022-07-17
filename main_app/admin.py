from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
from .models import Card, Series, Balance


@admin.register(Card)
class CardAdmin(ModelAdmin):
    pass


@admin.register(Series)
class SeriesAdmin(ModelAdmin):
    pass


@admin.register(Balance)
class SeriesAdmin(ModelAdmin):
    pass
