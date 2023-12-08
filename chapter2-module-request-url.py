from urllib.request import urlopen, Request
from pprint import pprint
import json

# with urlopen("https://www.example.com") as response:
#     body = response.read()
# print(body)

# url = "https://www.example.com"
# with urlopen(url) as response:
#     pass
#
# response.headers
# print('a')

# response = None
# try:
#     response = urlopen("https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview")
# except Exception as ex:
#     print(ex)
# else:
#     body = response.read()
# finally:
#     if response is not None:
#         response.close()

# decode the content of the website
# from urllib.request import urlopen
# with urlopen("https://www.example.com") as response:
#     body = response.read()
#
# character_set = response.headers.get_content_charset()
# decoded_body = body.decode(character_set)
# print(decoded_body[:30])

# decode the bytes to file
# with urlopen("https://www.google.com") as response:
#     body = response.read()
# character_set = response.headers.get_content_charset()
# content = body.decode(character_set)
#
# with open("google.html", encoding="utf-8", mode="w") as file:
#     file.write(content)

# Going from bytes to dictionary
# with urlopen("https://httpbin.org/json") as response:
#     body = response.read()
# character_set = response.headers.get_content_charset()
# data = json.loads(body)
# print(data)

# Example of make request function
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def make_request(url):
    try:
        with urlopen(url, timeout=10) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")


test_website = make_request("https://httpstat.us/403")
print(test_website)


def make_request_newversion(url, headers=None):
    request = Request(url, headers=headers or {})
    try:
        with urlopen(request, timeout=10) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")


body, response = make_request_newversion(
    "https://www.httpbin.org/user-agent",
    {"User-Agent": "Real Python"})
print(body, response)
