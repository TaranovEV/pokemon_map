import folium

from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from pokemon_entities.models import *


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon in pokemons:
        for entity in pokemon.entitys.all():
            add_pokemon(
                folium_map, entity.Lat,
                entity.Lon,
                (request.build_absolute_uri(pokemon.image.url)
                    if pokemon.image else None),
            )    

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url if pokemon.image else None,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon_on_page = {
        'pokemon_id': pokemon.id,
        'img_url': (pokemon.image.url
        if pokemon.image else None),
         'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
            }
    if pokemon.next_evolution is not None:
            pokemon_on_page['next_evolution'] = {
                'title_ru': pokemon.next_evolution.title,
                'pokemon_id': pokemon.next_evolution.id,
                'img_url': (pokemon.next_evolution.image.url
                if pokemon.next_evolution.image else None),
                            }
    try:
        pokemon_on_page['previous_evolution'] = {
                'title_ru': pokemon.previous_evolutions.get().title,
                'pokemon_id': pokemon.previous_evolutions.get().id,
                'img_url': (pokemon.previous_evolutions.get().image.url
                    if pokemon.previous_evolutions.get().next_evolution.image
                    else None),
                            }
    except Pokemon.DoesNotExist:
        pass

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon.entitys.filter(Pokemon=pokemon):
        add_pokemon(
            folium_map, pokemon_entity.Lat,
            pokemon_entity.Lon,
            (request.build_absolute_uri(pokemon.image.url)
                if pokemon.image else None)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_on_page
    })
