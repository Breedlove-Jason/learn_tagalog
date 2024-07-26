# package name is google-cloud-texttospeech
import os
import pandas as pd
from dotenv import load_dotenv
from google.cloud import texttospeech_v1 as texttospeech
from google.oauth2 import service_account

from translate_service import TranslationService
from tts_service import TextToSpeechService
from data_service import DataManagement

load_dotenv()

# Access the API key
API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")
SERVICE_ACCOUNT = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT)

client = texttospeech.TextToSpeechClient(credentials=credentials)

translation_service = TranslationService(API_KEY)
tts_service = TextToSpeechService(SERVICE_ACCOUNT)
data_manager = DataManagement()


def main():
    file_path = "data/translations.csv"
    if not os.path.exists(file_path):
        # Assuming the translations need to be generated
        source_file = "data/wordlist.txt"
        df = pd.read_csv(source_file, sep=" ")
        tagalog_words = df.iloc[:, 0].tolist()
        translation_dict = {word: translation_service.translate_word(word) for word in tagalog_words}
        data_manager.save_translations_to_csv(translation_dict, file_path)
    else:
        df = pd.read_csv(file_path)
        tagalog_words = df['Tagalog'].tolist()

    # Generate audio files if they do not exist
    for word, english in zip(df['Tagalog'], df['English']):
        audio_file_path = f"audio/{word}.mp3"
        if not os.path.exists(audio_file_path):
            tts_service.text_to_speech(english, audio_file_path)


if __name__ == '__main__':
    main()