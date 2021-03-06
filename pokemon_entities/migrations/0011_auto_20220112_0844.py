# Generated by Django 3.1.14 on 2022-01-12 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20220111_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, upload_to='pokemon_entities', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolutions', to='pokemon_entities.pokemon', verbose_name='Следующая эволюция'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(max_length=200, null=True, verbose_name='Название на японском'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Appeared_at',
            field=models.DateTimeField(blank=True, verbose_name='Когда Появится?'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Defence',
            field=models.IntegerField(blank=True, default=0, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Disappeared_at',
            field=models.DateTimeField(blank=True, verbose_name='Когда исчезнет?'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Healts',
            field=models.IntegerField(blank=True, default=0, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Level',
            field=models.IntegerField(default=0, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Lon',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Stamina',
            field=models.IntegerField(blank=True, default=0, verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Strength',
            field=models.IntegerField(blank=True, default=0, verbose_name='Сила'),
        ),
    ]
