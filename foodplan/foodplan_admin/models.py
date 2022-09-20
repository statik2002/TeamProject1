from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html, mark_safe


class Ingredient(models.Model):
    name = models.CharField('Наименование', max_length=200)
    price = models.FloatField('Цена')
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient-detail', kwargs={'pk': self.pk})


class Meal(models.Model):
    name = models.CharField('Наименование', max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to='meals', null=True, blank=True)
    is_available = models.BooleanField('Доступно к показу', default=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal-detail', kwargs={'pk': self.pk})

    @admin.display(description='Общая стоимость')
    def get_total_price(self):
        ingredients = Ingredient.objects.all()
        total = 0
        for ingredient in ingredients:
            total += ingredient.price

        return total

    @admin.display(description='Кол-во ингредиентов')
    def ingredients_count(self):
        return format_html(
            f'<span style="color:red">{Ingredient.objects.all().count()}</span>'
        )

    @admin.display(description='картинка')
    def image_thumbnails(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        else:
            return mark_safe('<span>No image</span>')
