import requests_with_caching
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
params = parameters
permanent_cache_file = "itunes_cache.txt"

iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params, permanent_cache_file)

py_data = json.loads(iTunes_response.text)

for x in py_data['results']:
    print(x['trackName'])
