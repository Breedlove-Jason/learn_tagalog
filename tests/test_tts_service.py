from dotenv import load_dotenv
import unittest
import os
from tts_service import TextToSpeechService

load_dotenv()


class TestTextToSpeechService(unittest.TestCase):
    def setUp(self):
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self.tts_service = TextToSpeechService(credentials_path)

    def test_text_to_speech(self):
        test_output_file = "../test_output.mp3"
        self.tts_service.text_to_speech("Hello, world!", test_output_file)
        self.assertTrue(os.path.exists(test_output_file))
        os.remove(test_output_file)

    def test_empty_text(self):
        test_output_file = "test_empty_output.mp3"
        self.tts_service.text_to_speech("", test_output_file)
        self.assertFalse(os.path.exists(test_output_file))


if __name__ == '__main__':
    unittest.main()
