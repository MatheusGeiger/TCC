# -*- coding:utf-8 -*-

import simplejson, urllib


def ControlerGetAddress(latitude, longitude):
    origem_viagem = '%s,%s' % (latitude , longitude)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyBC4a11g-stHdlMa7F89GlytBEWQ09Ww_o'%origem_viagem
    result = simplejson.load(urllib.urlopen(url))
    endereco = result['results'][0]['formatted_address']
    return endereco

def ControlerGetDistance(destino, latitude, longitude):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s,%s&key=AIzaSyCjWqMAxszBJAEwdxfGhRdvUGsN8eYyDZM" % (destino, latitude, longitude)
    result = simplejson.load(urllib.urlopen(url))
    json_distance = simplejson.dumps(result['rows'][0]['elements'][0]['distance']['value'], indent=2)
    if (int(json_distance) < 500):
        return True
    else:
        return False
