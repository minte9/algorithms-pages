""" API Cache
Example of using hash table to implement a caching system

Frozenset() ensures key consistency, will get the same hash string.
In a set() params order doesn't matter, but after hashing the result is not the same.
"""

import requests
from icecream import ic

class APICache:
    def __init__(self):
        self.cache = {} # dictionary (hash table)

    def fetch_data(self, url, params):
        
        # Generate a unique cache key based on the URL and parameters
        key = (url, frozenset(params.items()))
        ic("Request", hash(key))

        if key in self.cache:
            ic("Cache", self.cache[key])
            return self.cache[key]
        else:
            # Make the API request
            response = requests.get(url, params)
            data = response.json()
            ic("Response", response.json())

            # Cache the response for future use
            self.cache[key] = data
            return data

# Example usage
api = APICache()

# First API request
data = api.fetch_data("http://echo.jsontest.com/a/1/b/2", {"a":1, "b":2})

# Second API request (same params)
data = api.fetch_data("http://echo.jsontest.com/a/1/b/2", {"a":1, "b":2})

# Third API request (same params - diffent set orders)
data = api.fetch_data("http://echo.jsontest.com/a/1/b/2", {"b":2, "a":1})

"""
    ic| 'Request', hash(key): 7003653728631573416
    ic| 'Response', response.json(): {'a': '1', 'b': '2'}
    ic| 'Request', hash(key): 7003653728631573416
    ic| 'Cache', self.cache[key]: {'a': '1', 'b': '2'}
    ic| 'Request', hash(key): 7003653728631573416
    ic| 'Cache', self.cache[key]: {'a': '1', 'b': '2'}
"""