import json
import requests

startUrl = "http://gateway.marvel.com/v1/public/comics?ts=1&apikey="
md5hash = "&hash=28e5d831e56dd3365f0a701589fff1c4"
api_key = "fe263a50ca84b40f2bbd53b362f73800"

response = requests.get(startUrl + api_key + md5hash).json()
print(json.dumps(response, indent=4, sort_keys=True))
