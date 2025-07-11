import requests

# API to predict age by name
url = 'https://api.agify.io'

# Parameters sent as a dictionary
params = {'name': 'monika'}

response = requests.get(url, params=params)

data = response.json()
print(f"Name: {data['name']}")
print(f"Predicted Age: {data['age']}")
print(f"Count: {data['count']}")

print("Status Code:", response.status_code)
print("Response Body:", response.json())  # Parsed JSON response
