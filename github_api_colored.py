import requests
import json
from colorama import init, Fore, Style
from datetime import datetime

# Initialize colorama
init(autoreset=True)

def get_github_api_data():
    """Fetch GitHub API root endpoint data"""
    url = 'https://api.github.com'
    
    print(Fore.CYAN + Style.BRIGHT + "🌐 Fetching GitHub API Data..." + Style.RESET_ALL)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print(Fore.GREEN + f"✅ Successfully fetched data (Status: {response.status_code})" + Style.RESET_ALL)
        return data
        
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"❌ Error fetching data: {e}" + Style.RESET_ALL)
        return None

def save_to_file(data, filename):
    """Save data to a file with beautiful formatting"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write header
            file.write("=" * 80 + "\n")
            file.write("🌐 GITHUB API ENDPOINTS\n")
            file.write("=" * 80 + "\n")
            file.write(f"📅 Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"📊 Total endpoints: {len(data)}\n")
            file.write("=" * 80 + "\n\n")
            
            # Categorize endpoints
            categories = {
                "👤 User Management": [],
                "📦 Repository Management": [],
                "🔍 Search": [],
                "📝 Content Management": [],
                "🔐 Authentication": [],
                "📢 Notifications": [],
                "🏢 Organizations": [],
                "📊 Analytics": [],
                "🎨 Miscellaneous": []
            }
            
            # Categorize each endpoint
            for key, value in data.items():
                if 'user' in key.lower():
                    categories["👤 User Management"].append((key, value))
                elif 'repo' in key.lower() or 'gist' in key.lower():
                    categories["📦 Repository Management"].append((key, value))
                elif 'search' in key.lower():
                    categories["🔍 Search"].append((key, value))
                elif 'issue' in key.lower() or 'pull' in key.lower() or 'commit' in key.lower():
                    categories["📝 Content Management"].append((key, value))
                elif 'auth' in key.lower() or 'token' in key.lower():
                    categories["🔐 Authentication"].append((key, value))
                elif 'notification' in key.lower():
                    categories["📢 Notifications"].append((key, value))
                elif 'org' in key.lower():
                    categories["🏢 Organizations"].append((key, value))
                elif 'rate' in key.lower() or 'limit' in key.lower():
                    categories["📊 Analytics"].append((key, value))
                else:
                    categories["🎨 Miscellaneous"].append((key, value))
            
            # Write categorized data
            for category, endpoints in categories.items():
                if endpoints:  # Only write categories that have endpoints
                    file.write(f"\n{category}\n")
                    file.write("-" * 60 + "\n")
                    
                    for key, value in endpoints:
                        file.write(f"🔗 {key}:\n")
                        file.write(f"   📍 {value}\n")
                        file.write("\n")
            
            # Write raw JSON at the end
            file.write("\n" + "=" * 80 + "\n")
            file.write("📄 RAW JSON DATA\n")
            file.write("=" * 80 + "\n")
            file.write(json.dumps(data, indent=2))
        
        print(Fore.GREEN + f"✅ Data saved to {filename}" + Style.RESET_ALL)
        return True
        
    except Exception as e:
        print(Fore.RED + f"❌ Error saving file: {e}" + Style.RESET_ALL)
        return False

def display_summary(data):
    """Display a summary of the GitHub API data"""
    print(Fore.YELLOW + "\n📊 GITHUB API SUMMARY:" + Style.RESET_ALL)
    print(Fore.CYAN + f"   Total endpoints: {len(data)}" + Style.RESET_ALL)
    
    # Count endpoints by category
    categories = {
        "User Management": sum(1 for key in data.keys() if 'user' in key.lower()),
        "Repository Management": sum(1 for key in data.keys() if 'repo' in key.lower() or 'gist' in key.lower()),
        "Search": sum(1 for key in data.keys() if 'search' in key.lower()),
        "Content Management": sum(1 for key in data.keys() if 'issue' in key.lower() or 'pull' in key.lower()),
        "Authentication": sum(1 for key in data.keys() if 'auth' in key.lower()),
        "Notifications": sum(1 for key in data.keys() if 'notification' in key.lower()),
        "Organizations": sum(1 for key in data.keys() if 'org' in key.lower()),
        "Analytics": sum(1 for key in data.keys() if 'rate' in key.lower()),
        "Miscellaneous": sum(1 for key in data.keys() if not any(x in key.lower() for x in ['user', 'repo', 'gist', 'search', 'issue', 'pull', 'auth', 'notification', 'org', 'rate']))
    }
    
    for category, count in categories.items():
        if count > 0:
            print(Fore.MAGENTA + f"   {category}: {count} endpoints" + Style.RESET_ALL)

def main():
    """Main function"""
    print(Fore.CYAN + Style.BRIGHT + "\n🚀 GitHub API Data Fetcher\n" + Style.RESET_ALL)
    
    # Fetch data
    data = get_github_api_data()
    
    if data:
        # Display summary
        display_summary(data)
        
        # Save to file
        filename = f"github_api_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        success = save_to_file(data, filename)
        
        if success:
            print(Fore.GREEN + f"\n🎉 Success! Check the file: {filename}" + Style.RESET_ALL)
            print(Fore.YELLOW + "💡 The file contains categorized endpoints and raw JSON data." + Style.RESET_ALL)
        else:
            print(Fore.RED + "\n❌ Failed to save file." + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n❌ Failed to fetch GitHub API data." + Style.RESET_ALL)

if __name__ == "__main__":
    main() 