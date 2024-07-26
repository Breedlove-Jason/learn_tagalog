import requests


class TranslationService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://translation.googleapis.com/language/translate/v2"

    def translate_word(self, word):
        params = {
            "q": word,
            "source": "tl",
            "target": "en",
            "format": "text",
            "key": self.api_key,
        }
        response = requests.get(self.base_url, params=params)
        result = response.json()
        return result["data"]["translations"][0]["translatedText"]
