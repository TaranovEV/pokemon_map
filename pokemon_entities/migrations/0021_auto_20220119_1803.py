# Generated by Django 3.1.14 on 2022-01-19 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_auto_20220119_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonelementtype',
            name='strong_against',
            field=models.ManyToManyField(blank=True, to='pokemon_entities.PokemonElementType', verbose_name='Strong against'),
        ),
    ]
