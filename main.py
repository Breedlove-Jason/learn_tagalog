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

<<<<<<< HEAD
# Access the API key
API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")
SERVICE_ACCOUNT = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT)

client = texttospeech.TextToSpeechClient(credentials=credentials)


# FILE = "tl_full.txt"
# df = pd.read_csv(FILE, sep=" ")
# tagalog_words = df.iloc[:, 0].tolist()
# # print(tagalog_words)
#
# # Example of translating the first word and printing it
# english_word = translate_word(tagalog_words[200])
# print(f"Tagalog: {tagalog_words[200]}, English: {english_word}")


# Assuming tagalog_words is already loaded and available
# translation_dict = create_translation_dict(tagalog_words)
# save_translations_to_csv(translation_dict, "translations.csv")
=======
API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")
SERVICE_ACCOUNT = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

translation_service = TranslationService(API_KEY)
tts_service = TextToSpeechService(SERVICE_ACCOUNT)
data_manager = DataManagement()


def main():
    file_path = "translations.csv"
    if not os.path.exists(file_path):
        # Assuming the translations need to be generated
        source_file = "tl_full.txt"
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
>>>>>>> a91b21e (tagalog audio files, test files)
