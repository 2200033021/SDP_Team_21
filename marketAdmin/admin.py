from django.contrib import admin
from .models import grocrey, vegitables, Platform, GroceryPlatform, VegetablePlatform


class GroceryPlatformInline(admin.TabularInline):
    model = GroceryPlatform
    extra = 1

class VegetablePlatformInline(admin.TabularInline):
    model = VegetablePlatform
    extra = 1


@admin.register(grocrey)
class GroceryAdmin(admin.ModelAdmin):
    list_display = ['id', 'gname', 'gprice', 'ginfo', 'gamm', 'gimg']
    inlines = [GroceryPlatformInline]


@admin.register(vegitables)
class VegetableAdmin(admin.ModelAdmin):
    list_display = ['id', 'vname', 'vprice', 'vinfo', 'vamm', 'vimg']
    inlines = [VegetablePlatformInline]


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name']
