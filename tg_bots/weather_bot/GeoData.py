from geopy.geocoders import Nominatim
from requests import get
from json import loads

#print(__name__)


class Geo:
    pass

#Получить координаты города -> citys
def posittion(city : str):
    geolocator = Nominatim(user_agent="telebot")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return (latitude, longitude)

#Получить код города
def code_location(latitude: str, longitude: str, token_accu: str):
    query = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={token_accu}&q={latitude},{longitude}&language=ru'
    resp_loc = get(query, headers={"APIKey": token_accu})
    json_data = loads(resp_loc.text)
    code = json_data['Key']
    return code