from django.contrib import admin

from .models import *


class IngredientAdmin(admin.ModelAdmin):
    pass


class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_thumbnails', 'ingredients_count', 'get_total_price', 'is_available')
    list_editable = ('name', 'is_available',)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Meal, MealAdmin)
