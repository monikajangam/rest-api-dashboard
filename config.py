"""
Configuration file for the Daily Dashboard & API Testing Suite
"""

# API Configuration
APIS = {
    'weather': {
        'base_url': 'https://wttr.in',
        'format': 'j1'
    },
    'joke': {
        'url': 'https://official-joke-api.appspot.com/random_joke'
    },
    'quote': {
        'url': 'https://zenquotes.io/api/random'
    },
    'age': {
        'url': 'https://api.agify.io'
    },
    'dog': {
        'url': 'https://dog.ceo/api/breeds/image/random'
    },
    'github': {
        'url': 'https://api.github.com'
    }
}

# Dashboard Configuration
DASHBOARD_CONFIG = {
    'default_city': 'New York',
    'log_directory': '.',
    'log_filename_format': 'dashboard_log_{date}.txt'
}

# Display Configuration
DISPLAY_CONFIG = {
    'colors': {
        'weather': 'green',
        'joke': 'magenta', 
        'quote': 'blue',
        'error': 'red',
        'success': 'yellow',
        'info': 'cyan'
    },
    'emojis': {
        'weather': '🌤️',
        'joke': '😄',
        'quote': '💭',
        'success': '✅',
        'error': '❌',
        'info': '📄'
    }
}

# Request Configuration
REQUEST_CONFIG = {
    'timeout': 10,
    'headers': {
        'User-Agent': 'Daily-Dashboard/1.0 (https://github.com/yourusername/RestApis)'
    }
} 