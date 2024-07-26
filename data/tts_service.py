from google.cloud import texttospeech_v1 as texttospeech
<<<<<<< HEAD
from google.oauth2 import service_account


# need to update credential paths
class TTSService:
    def __init__(self, credentials_path):
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path
        )
        self.client = texttospeech.TextToSpeechClient(credentials=credentials)

    def text_to_speech(self, text, language_code="en-US"):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        return response.audio_content

    def save_speech_to_file(self, audio_content, file_name):
        with open(file_name, "wb") as out:
            out.write(audio_content)
            print(f"Audio content written to file {file_name}")
=======
import os


class TextToSpeechService:
    def __init__(self, credentials_path):
        self.client = texttospeech.TextToSpeechClient.from_service_account_file(credentials_path)

    def text_to_speech(self, text, output_file, language_code='fil-PH'):
        if text.strip() == "":
            print("No text provided for TTS.")
            return
        if not os.path.exists(output_file):
            synthesis_input = texttospeech.SynthesisInput(text=text)
            voice = texttospeech.VoiceSelectionParams(
                language_code=language_code,  # Set this to 'fil-PH' for Tagalog
                ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )
            response = self.client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )
            with open(output_file, "wb") as out:
                out.write(response.audio_content)
                print(f'Audio content written to file "{output_file}"')
        else:
            print(f'Audio file "{output_file}" already exists.')
>>>>>>> a91b21e (tagalog audio files, test files)
