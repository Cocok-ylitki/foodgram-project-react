# Generated by Django 3.2.11 on 2022-04-20 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IngredientQuantity',
        ),
    ]
