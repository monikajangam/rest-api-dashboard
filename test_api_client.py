"""
Test script for the API client functionality
"""

from api_client import api_client
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def test_all_apis():
    """Test all available APIs"""
    print(Fore.CYAN + Style.BRIGHT + "\n🧪 Testing All APIs\n" + Style.RESET_ALL)
    
    # Test weather API
    print(Fore.YELLOW + "Testing Weather API..." + Style.RESET_ALL)
    weather_data = api_client.get_weather("New York")
    if weather_data:
        current_condition = weather_data['current_condition'][0]
        temp = current_condition['temp_C']
        weather_desc = current_condition['weatherDesc'][0]['value']
        print(Fore.GREEN + f"✅ Weather: {temp}°C, {weather_desc}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "❌ Weather API failed" + Style.RESET_ALL)
    
    # Test joke API
    print(Fore.YELLOW + "\nTesting Joke API..." + Style.RESET_ALL)
    joke_data = api_client.get_joke()
    if joke_data:
        print(Fore.GREEN + f"✅ Joke: {joke_data['setup']} - {joke_data['punchline']}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "❌ Joke API failed" + Style.RESET_ALL)
    
    # Test quote API
    print(Fore.YELLOW + "\nTesting Quote API..." + Style.RESET_ALL)
    quote_data = api_client.get_quote()
    if quote_data:
        quote = quote_data[0]
        print(Fore.GREEN + f"✅ Quote: \"{quote['q']}\" — {quote['a']}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "❌ Quote API failed" + Style.RESET_ALL)
    
    # Test age prediction API
    print(Fore.YELLOW + "\nTesting Age Prediction API..." + Style.RESET_ALL)
    age_data = api_client.get_age_prediction("Monika")
    if age_data:
        print(Fore.GREEN + f"✅ Age prediction for Monika: {age_data['age']} years" + Style.RESET_ALL)
    else:
        print(Fore.RED + "❌ Age prediction API failed" + Style.RESET_ALL)
    
    # Test dog image API
    print(Fore.YELLOW + "\nTesting Dog Image API..." + Style.RESET_ALL)
    dog_data = api_client.get_dog_image()
    if dog_data:
        print(Fore.GREEN + f"✅ Dog image URL: {dog_data['message']}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "❌ Dog image API failed" + Style.RESET_ALL)
    
    # Test GitHub API
    print(Fore.YELLOW + "\nTesting GitHub API..." + Style.RESET_ALL)
    github_data = api_client.test_github_api()
    if github_data:
        print(Fore.GREEN + f"✅ GitHub API: {github_data.get('current_user_url', 'Connected')}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "❌ GitHub API failed" + Style.RESET_ALL)

def test_specific_api():
    """Test a specific API based on user input"""
    print(Fore.CYAN + Style.BRIGHT + "\n🎯 Test Specific API\n" + Style.RESET_ALL)
    print("Available APIs:")
    print("1. Weather")
    print("2. Joke")
    print("3. Quote")
    print("4. Age Prediction")
    print("5. Dog Image")
    print("6. GitHub")
    
    choice = input(Fore.YELLOW + "\nEnter your choice (1-6): " + Style.RESET_ALL).strip()
    
    if choice == "1":
        city = input("Enter city name: ").strip()
        weather_data = api_client.get_weather(city)
        if weather_data:
            current_condition = weather_data['current_condition'][0]
            temp = current_condition['temp_C']
            weather_desc = current_condition['weatherDesc'][0]['value']
            print(Fore.GREEN + f"✅ Weather in {city}: {temp}°C, {weather_desc}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Weather API failed" + Style.RESET_ALL)
    
    elif choice == "2":
        joke_data = api_client.get_joke()
        if joke_data:
            print(Fore.GREEN + f"✅ Joke: {joke_data['setup']} - {joke_data['punchline']}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Joke API failed" + Style.RESET_ALL)
    
    elif choice == "3":
        quote_data = api_client.get_quote()
        if quote_data:
            quote = quote_data[0]
            print(Fore.GREEN + f"✅ Quote: \"{quote['q']}\" — {quote['a']}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Quote API failed" + Style.RESET_ALL)
    
    elif choice == "4":
        name = input("Enter name: ").strip()
        age_data = api_client.get_age_prediction(name)
        if age_data:
            print(Fore.GREEN + f"✅ Age prediction for {name}: {age_data['age']} years" + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Age prediction API failed" + Style.RESET_ALL)
    
    elif choice == "5":
        dog_data = api_client.get_dog_image()
        if dog_data:
            print(Fore.GREEN + f"✅ Dog image URL: {dog_data['message']}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Dog image API failed" + Style.RESET_ALL)
    
    elif choice == "6":
        github_data = api_client.test_github_api()
        if github_data:
            print(Fore.GREEN + f"✅ GitHub API: {github_data.get('current_user_url', 'Connected')}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ GitHub API failed" + Style.RESET_ALL)
    
    else:
        print(Fore.RED + "❌ Invalid choice" + Style.RESET_ALL)

def main():
    """Main function"""
    print(Fore.CYAN + Style.BRIGHT + "\n🚀 API Client Test Suite\n" + Style.RESET_ALL)
    
    while True:
        print("\nOptions:")
        print("1. Test all APIs")
        print("2. Test specific API")
        print("3. Exit")
        
        choice = input(Fore.YELLOW + "\nEnter your choice (1-3): " + Style.RESET_ALL).strip()
        
        if choice == "1":
            test_all_apis()
        elif choice == "2":
            test_specific_api()
        elif choice == "3":
            print(Fore.GREEN + "👋 Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "❌ Invalid choice" + Style.RESET_ALL)

if __name__ == "__main__":
    main() 