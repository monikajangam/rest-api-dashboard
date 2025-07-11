import requests

# The URL you want to send the GET request to
url = 'https://api.github.com'  # Public API, no login needed

# Sending the GET request
response = requests.get(url)

# Print the HTTP status code
print("Status Code:", response.status_code)

# Print the returned data in text
print("Response Body:")

print(response.text)
