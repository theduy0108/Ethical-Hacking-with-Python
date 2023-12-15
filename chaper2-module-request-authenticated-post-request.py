from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
from urllib.parse import urlencode


def make_request(url, headers=None, data=None):
    request = Request(url, headers=headers or {}, data=data)
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


post_dict = {"Title": "Hello World", "Name": "Real Python"}
url_encoded_data = urlencode(post_dict)
post_data = url_encoded_data.encode("utf-8")
print(post_data)
body, response = make_request("https://httpbin.org/anything", data=post_data)
print(body.decode("utf-8"))