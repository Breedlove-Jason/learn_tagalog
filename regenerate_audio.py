import os
import pandas as pd
from tts_service import TextToSpeechService
from dotenv import load_dotenv


def main():
    # Ensure environment variables are loaded (if stored in .env)
    load_dotenv()

    # Path to the CSV file that contains translations
    csv_file_path = 'translations.csv'
    # Assuming the CSV has a column 'Tagalog' for the Tagalog words
    df = pd.read_csv(csv_file_path)

    # Credentials for Text to Speech Service
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    tts_service = TextToSpeechService(credentials_path)

    # Iterate over each Tagalog word in the DataFrame
    for index, row in df.iterrows():
        tagalog_word = row['Tagalog']
        audio_file_path = f"audio/{tagalog_word}.mp3"
        tts_service.text_to_speech(tagalog_word, audio_file_path, language_code='fil-PH')


if __name__ == '__main__':
    main()
