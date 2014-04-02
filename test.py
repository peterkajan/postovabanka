import urllib

character = 1
query_params = {'chr' : character}
print '/results?' + urllib.urlencode(query_params)