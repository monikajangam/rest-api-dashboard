import requests
from colorama import init, Fore, Style
from datetime import datetime

# Initialize colorama
init(autoreset=True)

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
    print(Fore.YELLOW + f"\n✅ Dashboard saved to {filename}\n" + Style.RESET_ALL)

def view_past_log():
    date = input(Fore.CYAN + "Enter the date of the log to view (YYYY-MM-DD): " + Style.RESET_ALL)
    filename = f"dashboard_log_{date}.txt"
    try:
        with open(filename, "r") as file:
            print(Fore.GREEN + "\n📄 Past Dashboard Log:\n" + Style.RESET_ALL)
            print(file.read())
    except FileNotFoundError:
        print(Fore.RED + f"\n❌ No log found for {date}.\n" + Style.RESET_ALL)

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n🌤️  Welcome to Your Extended Daily Dashboard\n")
    choice = input(Fore.YELLOW + "Type 'run' to get today's dashboard or 'view' to see a past log: " + Style.RESET_ALL).strip().lower()

    if choice == 'run':
        city = input(Fore.CYAN + "Enter your city: " + Style.RESET_ALL)
        print(Fore.YELLOW + "\nFetching your daily dashboard...\n" + Style.RESET_ALL)
        
        weather = get_weather(city)
        joke = get_joke()
        quote = get_quote()
        
        dashboard_output = f"{weather}\n{joke}\n{quote}"
        
        print(Fore.GREEN + weather + Style.RESET_ALL)
        print(Fore.MAGENTA + joke + Style.RESET_ALL)
        print(Fore.BLUE + quote + Style.RESET_ALL)

        save_choice = input(Fore.YELLOW + "\nDo you want to save this dashboard to a log file? (yes/no): " + Style.RESET_ALL).strip().lower()
        if save_choice == 'yes':
            save_to_log(dashboard_output)

    elif choice == 'view':
        view_past_log()
    else:
        print(Fore.RED + "\n❌ Invalid option. Please type 'run' or 'view'.\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
