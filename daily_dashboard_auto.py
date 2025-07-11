import requests
from datetime import datetime

def get_weather(city):
    url = f'https://wttr.in/{city}?format=j1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_condition = data['current_condition'][0]
        temp = current_condition['temp_C']
        weather_desc = current_condition['weatherDesc'][0]['value']
        return f"Weather in {city}: {temp}°C, {weather_desc}"
    else:
        return "Could not fetch weather data."

def get_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"Joke: {data['setup']} - {data['punchline']}"
    else:
        return "Could not fetch a joke."

def get_quote():
    url = 'https://zenquotes.io/api/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        return f"Quote: \"{data['q']}\" — {data['a']}"
    else:
        return "Could not fetch a quote."

def save_to_log(content):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"dashboard_log_{today}.txt"
    with open(filename, "w") as file:
        file.write(content)

def main():
    city = "New York"  # set your city here
    weather = get_weather(city)
    joke = get_joke()
    quote = get_quote()

    dashboard_output = f"{weather}\n{joke}\n{quote}"
    save_to_log(dashboard_output)

if __name__ == "__main__":
    main()
