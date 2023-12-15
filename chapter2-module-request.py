import requests

test_response = requests.get('https://api.github.com')

# Test the status_code
if test_response.status_code == 200:
    print("Success")
elif test_response.status_code == 404:
    print('Not Found.')
else:
    print("Undetected Error")

# Check the content of the request
print(test_response.content)
print(test_response.text)

# Print out the header
print(test_response.headers)



