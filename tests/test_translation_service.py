import os
import sys

# Append the directory above 'tests' to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest import TestCase, main
from unittest.mock import patch
from translate_service import TranslationService  # Import your actual class


class TestTranslationService(TestCase):
    def setUp(self):
        self.api_key = 'fake_api_key'
        self.translation_service = TranslationService(self.api_key)

    @patch('requests.get')  # Mock 'requests.get' to not actually perform an HTTP request
    def test_translate_word(self, mock_get):
        # Configure the mock to return a specific response
        mock_get.return_value.json.return_value = {
            "data": {
                "translations": [{"translatedText": "hello"}]
            }
        }

        # Call the service
        result = self.translation_service.translate_word('kamusta')
        # Assert the result
        self.assertEqual(result, "hello")

    # Additional tests...


if __name__ == '__main__':
    main()


    @patch('requests.get')
    def test_translate_word_empty_string(self, mock_get):
        # Configure the mock to return an empty translation
        mock_get.return_value.json.return_value = {
            "data": {
                "translations": [{"translatedText": ""}]
            }
        }

        # Call the service
        result = self.translation_service.translate_word('')
        self.assertEqual(result, '')


    @patch('requests.get')
    def test_translate_word_api_error(self, mock_get):
        # Simulate an API error response
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("API limit exceeded")

        with self.assertRaises(requests.exceptions.HTTPError):
            self.translation_service.translate_word('kamusta')

if __name__ == '__main__':
    unittest.main()
