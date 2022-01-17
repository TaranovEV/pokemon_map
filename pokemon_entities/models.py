from django.db import models


class Pokemon(models.Model):
    title = models.CharField('Название', max_length=200, default='')
    image = models.ImageField('Изображение',
                              upload_to='pokemon_entities',
                              blank=True)
    description = models.TextField('Описание', blank=True)
    title_en = models.CharField('Название на английском',
                                max_length=200,
                                default='')
    title_jp = models.CharField('Название на японском',
                                max_length=200,
                                default='')
    next_evolution = models.ForeignKey('Pokemon',
                                       on_delete=models.SET_NULL,
                                       related_name='previous_evolutions',
                                       null=True,
                                       blank=True,
                                       verbose_name='Следующая эволюция',)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                verbose_name='Покемон',
                                related_name='exemplar_pokemon',)
    Lat = models.FloatField(verbose_name='Широта',)
    Lon = models.FloatField(verbose_name='Долгота',)
    Appeared_at = models.DateTimeField(verbose_name='Когда Появится?',
                                       blank=True, null=True)
    Disappeared_at = models.DateTimeField(verbose_name='Когда исчезнет?',
                                          blank=True, null=True)
    Level = models.IntegerField(default=0, verbose_name='Уровень',)
    Healts = models.IntegerField(default=0, verbose_name='Здоровье',
                                 blank=True)
    Strength = models.IntegerField(default=0, verbose_name='Сила',
                                   blank=True)
    Defence = models.IntegerField(default=0, verbose_name='Защита',
                                  blank=True)
    Stamina = models.IntegerField(default=0, verbose_name='Выносливость',
                                  blank=True)
