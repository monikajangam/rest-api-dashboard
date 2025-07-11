"""
Centralized API client for handling all external API requests
"""

import requests
import logging
from typing import Dict, Any, Optional
from config import APIS, REQUEST_CONFIG

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:
    """Centralized client for handling API requests"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(REQUEST_CONFIG['headers'])
        self.timeout = REQUEST_CONFIG['timeout']
    
    def _make_request(self, url: str, params: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
        """
        Make a GET request to the specified URL
        
        Args:
            url: The URL to request
            params: Optional query parameters
            
        Returns:
            JSON response data or None if request failed
        """
        try:
            logger.info(f"Making request to: {url}")
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed for {url}: {str(e)}")
            return None
        except ValueError as e:
            logger.error(f"Failed to parse JSON response from {url}: {str(e)}")
            return None
    
    def get_weather(self, city: str) -> Optional[Dict[str, Any]]:
        """Get weather data for a city"""
        url = f"{APIS['weather']['base_url']}/{city}"
        params = {'format': APIS['weather']['format']}
        return self._make_request(url, params)
    
    def get_joke(self) -> Optional[Dict[str, Any]]:
        """Get a random joke"""
        return self._make_request(APIS['joke']['url'])
    
    def get_quote(self) -> Optional[Dict[str, Any]]:
        """Get a random inspirational quote"""
        return self._make_request(APIS['quote']['url'])
    
    def get_age_prediction(self, name: str) -> Optional[Dict[str, Any]]:
        """Get age prediction for a name"""
        params = {'name': name}
        return self._make_request(APIS['age']['url'], params)
    
    def get_dog_image(self) -> Optional[Dict[str, Any]]:
        """Get a random dog image"""
        return self._make_request(APIS['dog']['url'])
    
    def test_github_api(self) -> Optional[Dict[str, Any]]:
        """Test GitHub API connectivity"""
        return self._make_request(APIS['github']['url'])


# Global API client instance
api_client = APIClient() 