# 🌤️ REST API Dashboard

A Python project demonstrating REST API integrations with a daily dashboard featuring weather, jokes, quotes, and more.

## ✨ Features

I wanted to practice working with APIs, so I created this dashboard that pulls data from different sources:

## 🚀 Quick Start

```bash
git clone https://github.com/monikajangam/rest-api-dashboard.git
cd rest-api-dashboard
pip install -r requirements.txt
```

Then run the dashboard:
```bash
python daily_dashboard.py
```

## How to Use

### Main Dashboard
```bash
python daily_dashboard.py
```
Just follow the prompts - it's pretty straightforward!

### Test All the APIs
```bash
python test_api_client.py
```
This lets you test each API individually.

### Check Out GitHub's API
```bash
python github_api_colored.py
```
This creates a nice file with all of GitHub's API endpoints.

## APIs I Used

I played around with these APIs:
- **wttr.in** - for weather data
- **Official Joke API** - for random jokes
- **ZenQuotes** - for inspirational quotes
- **Agify.io** - for age prediction
- **Dog CEO API** - for dog images
- **GitHub API** - for GitHub stuff

## Project Files

Here's what's in this project:
```
rest-api-dashboard/
├── daily_dashboard.py        # The main dashboard
├── daily_dashboard_auto.py   # Automated version
├── test_api_client.py        # Testing tool
├── github_api_colored.py     # GitHub API explorer
├── api_client.py             # Handles all API calls
├── config.py                 # Settings
└── requirements.txt          # What you need to install
```

## What I Learned

This project helped me understand:
- How to work with different REST APIs
- Error handling in Python
- Making nice command-line interfaces
- Organizing code properly
- Testing my code

