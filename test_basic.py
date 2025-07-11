"""
Basic tests for the Daily Dashboard & API Testing Suite
"""

import pytest
from unittest.mock import Mock, patch
from api_client import APIClient
from config import APIS, DASHBOARD_CONFIG


class TestAPIClient:
    """Test cases for the APIClient class"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.client = APIClient()
    
    def test_client_initialization(self):
        """Test that the API client initializes correctly"""
        assert self.client.session is not None
        assert self.client.timeout == 10
        assert 'User-Agent' in self.client.session.headers
    
    @patch('requests.Session.get')
    def test_successful_request(self, mock_get):
        """Test successful API request"""
        # Mock successful response
        mock_response = Mock()
        mock_response.json.return_value = {'test': 'data'}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = self.client._make_request('https://test.api.com')
        
        assert result == {'test': 'data'}
        mock_get.assert_called_once()
    
    @patch('requests.Session.get')
    def test_failed_request(self, mock_get):
        """Test failed API request"""
        # Mock failed response
        mock_get.side_effect = Exception("Connection error")
        
        result = self.client._make_request('https://test.api.com')
        
        assert result is None


class TestConfiguration:
    """Test cases for configuration settings"""
    
    def test_apis_configuration(self):
        """Test that API configuration is properly structured"""
        assert 'weather' in APIS
        assert 'joke' in APIS
        assert 'quote' in APIS
        assert 'age' in APIS
        assert 'dog' in APIS
        assert 'github' in APIS
    
    def test_dashboard_configuration(self):
        """Test that dashboard configuration is properly structured"""
        assert 'default_city' in DASHBOARD_CONFIG
        assert 'log_directory' in DASHBOARD_CONFIG
        assert 'log_filename_format' in DASHBOARD_CONFIG
    
    def test_weather_api_config(self):
        """Test weather API configuration"""
        assert APIS['weather']['base_url'] == 'https://wttr.in'
        assert APIS['weather']['format'] == 'j1'
    
    def test_joke_api_config(self):
        """Test joke API configuration"""
        assert 'random_joke' in APIS['joke']['url']
    
    def test_quote_api_config(self):
        """Test quote API configuration"""
        assert 'zenquotes.io' in APIS['quote']['url']


def test_imports():
    """Test that all modules can be imported successfully"""
    try:
        from api_client import api_client
        from config import APIS, DASHBOARD_CONFIG, DISPLAY_CONFIG, REQUEST_CONFIG
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import modules: {e}")


if __name__ == "__main__":
    pytest.main([__file__]) 