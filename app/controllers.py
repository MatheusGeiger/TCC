# -*- coding:utf-8 -*-

import simplejson, urllib


def ControlerGetAddress(latitude, longitude):
    origem_viagem = '%s,%s' % (latitude , longitude)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s'%origem_viagem
    result = simplejson.load(urllib.urlopen(url))
    endereco = result['results'][0]['formatted_address']
    return endereco
