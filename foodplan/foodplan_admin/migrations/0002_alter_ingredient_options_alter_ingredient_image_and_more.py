# Generated by Django 4.1.1 on 2022-09-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplan_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
