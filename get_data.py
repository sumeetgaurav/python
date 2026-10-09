"""Minimal example of fetching JSON data from a REST API using the requests library."""

import requests
url = "https://fake-json-api.mock.beeceptor.com/users"

response = requests.get(url=url)
print(response.json())