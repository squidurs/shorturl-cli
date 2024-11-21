import unittest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from shorturl.commands import *

class TestCliCommands(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch('requests.post')
    def test_login_successful(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"access_token": "test_token"})
        
        result = self.runner.invoke(login, ['--username', 'testuser', '--password', 'testpass'])
        self.assertIn("Login successful.", result.output)
        self.assertEqual(result.exit_code, 0)
        
    @patch('requests.post')
    def test_login_fail(self, mock_post):
        mock_post.return_value = MagicMock(status_code=401)
        
        result = self.runner.invoke(login, ['--username', 'testuser', '--password', 'testpass'])
        self.assertIn("401", result.output)
        self.assertEqual(result.exit_code, 0)
        
    @patch('requests.post')
    def test_create_new_user(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"message": "User created successfully."})
        
        result = self.runner.invoke(register, ['--username', 'testuser', '--password', 'testpass'])
        self.assertIn("User testuser created successfully.", result.output)
        self.assertEqual(result.exit_code, 0)

    @patch('requests.post')
    def test_shorten_url(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {'short_url': 'testurl', 'original_url': 'https://example.com/'})

        result = self.runner.invoke(shorten, ['--url', 'https://example.com'])
        self.assertIn("Short URL created: testurl", result.output)
        self.assertEqual(result.exit_code, 0)
        
    @patch('requests.post')
    def test_shorten_url_error409(self, mock_post):
        mock_post.return_value = MagicMock(status_code=409, text="This custom URL is already in use.")

        result = self.runner.invoke(shorten, ['--url', 'https://example.com', '--custom', 'takenurl'])
        self.assertIn("409 - This custom URL is already in use.", result.output)
        self.assertEqual(result.exit_code, 0)
        
    @patch('requests.post')
    def test_shorten_url_error403(self, mock_post):
        mock_post.return_value = MagicMock(status_code=403, text="URL limit reached.")

        result = self.runner.invoke(shorten, ['--url', 'https://example.com'])
        self.assertIn("403 - URL limit reached.", result.output)
        self.assertEqual(result.exit_code, 0)
        
    @patch('requests.get')
    def test_list_my_urls(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"url_pairs": {"short_url": "abc123", "original_url": "http://example.com"}})
        
        result = self.runner.invoke(list, ['--my'])
        self.assertIn("abc123", result.output)
        self.assertEqual(result.exit_code, 0)
        
    @patch('requests.get')
    def test_list_my_urls_error(self, mock_get):
        mock_get.return_value = MagicMock(status_code=404, text="You don't have any shortened URLs")
        
        result = self.runner.invoke(list, ['--my'])
        self.assertIn("404 - You don't have any shortened URLs", result.output)
        self.assertEqual(result.exit_code, 0)
        
    @patch('requests.get')
    def test_list_all_urls(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"url_pairs": {"short_url": "abc123", "original_url": "http://example.com"}})
        
        result = self.runner.invoke(list, ['--all'])
        self.assertIn("abc123", result.output)
        self.assertEqual(result.exit_code, 0)

    @patch('requests.get')
    def test_list_all_urls_unauthorized(self, mock_get):
        mock_get.return_value = MagicMock(status_code=403, text="Admin privileges are required.")
        
        result = self.runner.invoke(list, ['--all'])
        self.assertIn("403 - Admin privileges are required", result.output)
        self.assertEqual(result.exit_code, 0)
    
    @patch('requests.get')
    def test_lookup_url(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"original_url": "http://example.com"})
        
        result = self.runner.invoke(lookup, ['--short', 'abc123'])
        self.assertIn("http://example.com", result.output)
        self.assertEqual(result.exit_code, 0)
        
    @patch('requests.get')
    def test_lookup_url_error(self, mock_get):
        mock_get.return_value = MagicMock(status_code=404, text="Short URL not found")
        
        result = self.runner.invoke(lookup, ['--short', 'abc123'])
        self.assertIn("Short URL not found", result.output)
        self.assertEqual(result.exit_code, 0)
        
    @patch('requests.post')
    def test_change_password(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"message": "Password has been updated."})
        
        result = self.runner.invoke(change_password, ['--username', 'testuser', '--password', 'testpass'])
        self.assertIn('Password changed successfully.', result.output)
        self.assertEqual(result.exit_code, 0)
        

