# -*- coding:utf-8 -*-

import simplejson, urllib
from unicodedata import normalize
from django.contrib import messages
import requests
from django.http import HttpResponseRedirect

def ControlerGetAddress(latitude, longitude):
    origem_viagem = '%s,%s' % (latitude , longitude)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyBC4a11g-stHdlMa7F89GlytBEWQ09Ww_o'%origem_viagem
    result = simplejson.load(urllib.urlopen(url))
    endereco = result['results'][0]['formatted_address']
    return endereco

def ControlerGetDistance(destino, latitude, longitude):
    try:
        destino = normalize("NFKD", unicode(destino)).encode('ascii', 'ignore')
        try:
            url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s,%s" % (destino, latitude, longitude)
            result = simplejson.load(urllib.urlopen(url))
            json_distance = simplejson.dumps(result['rows'][0]['elements'][0]['distance']['value'], indent=2)
            if (int(json_distance) < 500):
                return True
            else:
                return False
        except:
            return 'erro'
    except:
        return False
