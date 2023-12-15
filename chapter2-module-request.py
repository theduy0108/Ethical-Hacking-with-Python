import requests

from requests.auth import HTTPBasicAuth
from getpass import getpass
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError


test_response = requests.get('https://api.github.com')

# Test the status_code
# if test_response.status_code == 200:
#     print("Success")
# elif test_response.status_code == 404:
#     print('Not Found.')
# else:
#     print("Undetected Error")
#
# # Check the content of the request
# print(test_response.content)
# print(test_response.text)
#
# # Print out the header
# print(test_response.headers)

# Query string parameters
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )
#
# # Inspect some attributes of the `requests` repository
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Repository name: {repository["name"]}')
# print(f'Repository description: {repository["description"]}')

# Request headers
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
#     headers={'Accept': 'application/vnd.github.v3.text-match+json'},
# )
# old_response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )
#
# # View the new `text-matches` array which provides information
# # about your search term within the results
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Text matches: {repository["text_matches"]}')

# Other HTTP Methods
# data = requests.post('https://httpbin.org/post', data={'key': 'duy'})
# data = requests.put('https://httpbin.org/put', data={'key': 'value'})
# data = requests.delete('https://httpbin.org/delete')
# data = requests.head('https://httpbin.org/get')
# data = requests.patch('https://httpbin.org/patch', data={'key': 'value'})
# data = requests.options('https://httpbin.org/get')

# Authentication
requests.get(
    'https://api.github.com/user',
    auth=HTTPBasicAuth('username', getpass())
)

# Time-out, max-retries
requests.get('https://api.github.com', timeout=1)

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
