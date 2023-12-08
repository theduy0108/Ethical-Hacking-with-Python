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
#

# Fixing the SSL CERTIFICATE_VERIFY_FAILED ERROR:
# from urllib.request import urlopen
# urlopen("https://superfish.badssl.com/") => create bugs

# import ssl
# unverified_context = ssl._create_unverified_context()
# urlopen("https://superfish.badssl.com/", context=unverified_context)

import ssl
from urllib.request import urlopen
import certifi
certifi_context = ssl.create_default_context(cafile=certifi.where())
urlopen("https://sha384.badssl.com/", context=certifi_context)


