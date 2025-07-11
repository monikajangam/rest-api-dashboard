# 🌤️ Daily Dashboard & API Testing Suite

A comprehensive Python project that demonstrates REST API interactions with multiple public APIs, featuring a daily dashboard with weather, jokes, and inspirational quotes.

## ✨ Features

### 🎯 API Testing Suite
- **Age Prediction API** - Predict age by name using agify.io
- **Dog Image API** - Fetch random dog images from Dog CEO API
- **GitHub API** - Basic GET request testing
- **HTTP Request Testing** - REST client file for API testing

### 🌤️ Daily Dashboard
- **Weather Information** - Real-time weather data for any city
- **Daily Jokes** - Random jokes to brighten your day
- **Inspirational Quotes** - Motivational quotes from famous personalities
- **Interactive Mode** - User-friendly command-line interface
- **Automated Mode** - Run without user input for scheduled tasks
- **Logging System** - Save and view past dashboard outputs
- **Colored Output** - Beautiful terminal interface with colorama

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/RestApis.git
   cd RestApis
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Interactive Dashboard
```bash
python daily_dashboard.py
```
- Choose 'run' to get today's dashboard
- Choose 'view' to see past logs
- Enter your city for weather information
- Option to save dashboard to log file

### Automated Dashboard
```bash
python daily_dashboard_auto.py
```
- Runs automatically with predefined city
- Saves output to daily log file
- Perfect for cron jobs or scheduled tasks

### API Testing
```bash
# Age prediction
python get_api.py

# Random dog image
python get_api_dog.py

# GitHub API test
python get_request_test.py
```

## 🛠️ APIs Used

| API | Purpose | Endpoint |
|-----|---------|----------|
| **wttr.in** | Weather data | `https://wttr.in/{city}?format=j1` |
| **Official Joke API** | Random jokes | `https://official-joke-api.appspot.com/random_joke` |
| **ZenQuotes** | Inspirational quotes | `https://zenquotes.io/api/random` |
| **Agify.io** | Age prediction | `https://api.agify.io` |
| **Dog CEO API** | Random dog images | `https://dog.ceo/api/breeds/image/random` |
| **GitHub API** | API testing | `https://api.github.com` |

## 📁 Project Structure

```
RestApis/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── daily_dashboard.py        # Interactive dashboard
├── daily_dashboard_auto.py   # Automated dashboard
├── get_api.py               # Age prediction API
├── get_api_dog.py           # Dog image API
├── get_request_test.py      # GitHub API test
├── rest.http                # HTTP request file
├── dashboard_log_*.txt      # Dashboard logs
└── venv/                    # Virtual environment
```

## 🔧 Configuration

### Customizing the Automated Dashboard
Edit `daily_dashboard_auto.py` to change the default city:
```python
city = "Your City Name"  # Change this line
```

### Adding New APIs
The modular structure makes it easy to add new API integrations:
1. Create a new function following the existing pattern
2. Add error handling for API responses
3. Integrate into the dashboard if desired

## 📊 Sample Output

```
🌤️  Welcome to Your Extended Daily Dashboard

Type 'run' to get today's dashboard or 'view' to see a past log: run
Enter your city: New York

Fetching your daily dashboard...

Weather in New York: 29°C, Partly cloudy
Joke: What's the best time to go to the dentist? - Tooth hurty.
Quote: "Be patient and calm; no one can catch fish in anger." — Herbert Hoover

Do you want to save this dashboard to a log file? (yes/no): yes

✅ Dashboard saved to dashboard_log_2025-01-27.txt
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [wttr.in](https://wttr.in) for weather data
- [Official Joke API](https://official-joke-api.appspot.com) for jokes
- [ZenQuotes](https://zenquotes.io) for inspirational quotes
- [Agify.io](https://agify.io) for age prediction
- [Dog CEO API](https://dog.ceo) for dog images

## 📞 Contact

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Email**: your.email@example.com

---

⭐ **Star this repository if you found it helpful!** 