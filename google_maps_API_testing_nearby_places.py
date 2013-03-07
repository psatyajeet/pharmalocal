import requests

lat = '40.798'
long = '-73.968'
key = 'AIzaSyBy81o-nlJ4RE6zuRwUaq87DZti5sK2f50'
radius = '5000'

URL = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?location=' + lat + ',' + long + '&radius=' + radius + '&types=pharmacy&sensor=false&key=' + key

print URL

print requests.get(URL)