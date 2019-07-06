"""
Overpass OpenStreetMap API to get all petanque (boules) terrain.
See https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide for the overpass API guide.
See https://github.com/mvexel/overpass-api-python-wrapper for the Python wrapper.
"""
import requests
import time

import overpass
api = overpass.API(timeout=60)


def get_terrains_world(responseformat='json'):
    stepsize = 4.0
    lon_begin = -180
    lon_end = 180
    lat_begin = -90
    lat_end = 90
    responses = []
    lon_current = lon_begin
    while lon_current < lon_end:
        lat_current = lat_begin
        while lat_current < lat_end:
            coordinate_str = '{},{},{},{}'.format(
                lat_current, lon_current, lat_current + stepsize, lon_current + stepsize
            )
            query = '''
            (
                node["sport" = "boules"]({});
                way["sport" = "boules"]({});
            )
            '''.format(coordinate_str, coordinate_str)
            print(query)
            start_time = time.time()
            try:
                response = api.get(query, responseformat=responseformat, verbosity='center')
            except (overpass.errors.MultipleRequestsError, overpass.errors.ServerLoadError) as error:
                print(error)
                time.sleep(30)
                response = api.get(query, responseformat=responseformat, verbosity='center')
            response_time = time.time() - start_time
            print('response time: ' + str(response_time), 'seconds')
            responses.append(response)
            lat_current += stepsize
            time.sleep(response_time * 2)
        lon_current += stepsize
    print('responses', str(len(responses)))
    return responses


def get_terrains_utrecht(responseformat='json'):
    query = '''(
        node["sport"="boules"](51.96203858429277,4.985389709472656,52.22296240972006,5.261421203613281);
        way["sport"="boules"](51.96203858429277,4.985389709472656,52.22296240972006,5.261421203613281);
        relation["sport"="boules"](51.96203858429277,4.985389709472656,52.22296240972006,5.261421203613281);
    )   
    '''
    return api.get(query, responseformat=responseformat, verbosity='center')  # use verbosity = geom to get way geometry in geojson


def get_terrains_nl(responseformat='json'):
    query = '''
    (area(3602323309);)->.searchArea;
    (
        node["sport" = "boules"](area.searchArea);
        way["sport" = "boules"](area.searchArea);
        relation["sport" = "boules"](area.searchArea);
    )
    '''
    return api.get(query, responseformat=responseformat, verbosity='center')


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
