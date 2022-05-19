# """
# 1. flickr api documentation- "https://www.flickr.com/services/api/flickr.photos.search.html"
# """

import requests_with_caching
import json
import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'f541de539b026763de2e9f36bd9dd437'


def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key
    params_diction["tags"] = tags_string
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests_with_caching.get(baseurl, params=params_diction, permanent_cache_file="flickr_cache.txt")
    print(flickr_resp.url)
    return flickr_resp.json()


result_river_mts = get_flickr_data("river,mountains")
photos = result_river_mts['photos']['photo']


for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = "https://www.flickr.com/photos/{}/{}".format(owner, photo_id)
    print(url)
    webbrowser.open(url)
