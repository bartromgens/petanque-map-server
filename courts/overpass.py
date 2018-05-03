"""
Overpass OpenStreetMap API to get all petanque (boules) courts.
See https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide for the overpass API guide.
See https://github.com/mvexel/overpass-api-python-wrapper for the Python wrapper.
"""
import requests

import overpass
api = overpass.API(timeout=25)


def get_courts_utrecht(responseformat='json'):
    query = '''(
        node["sport"="boules"](51.96203858429277,4.985389709472656,52.22296240972006,5.261421203613281);
        way["sport"="boules"](51.96203858429277,4.985389709472656,52.22296240972006,5.261421203613281);
        relation["sport"="boules"](51.96203858429277,4.985389709472656,52.22296240972006,5.261421203613281);
    )   
    '''
    return api.get(query, responseformat=responseformat, verbosity='center')  # use verbosity = geom to get way geometry in geojson


def get_courts_nl(responseformat='json'):
    query = '''
    (area[id="3602323309"];)->.searchArea;
    (
        node["sport" = "boules"](area.searchArea);
        way["sport" = "boules"](area.searchArea);
        relation["sport" = "boules"](area.searchArea);
    )
    '''
    return api.get(query, responseformat=responseformat)


def get_node(node_id, responseformat='json'):
    query = '(node(' + str(node_id) + ');)'
    return api.get(query, responseformat=responseformat)


def get_node_coordinates(node_id):
    node = get_node(node_id)
    return [node['elements'][0]['lon'], node['elements'][0]['lat']]


def get_country_area_id():
    query = '''
        (area["ISO3166-1"="NL"];)
    '''
    return api.get(query, responseformat='json')


def get_api_status():
    return requests.get('https://overpass-api.de/api/status')


def kill_my_queries():
    return requests.get('https://overpass-api.de/api/kill_my_queries')
