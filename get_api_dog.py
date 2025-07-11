import requests

url = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(url)
data = response.json()

print("Random dog image URL:", data['message'])
