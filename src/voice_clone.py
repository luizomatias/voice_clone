"""
Voice Generator class
Autor: LuizoMatias
"""
import os
import tempfile
import requests
from dotenv import load_dotenv, find_dotenv
from elevenlabs import set_api_key, voices

load_dotenv(find_dotenv(), override=True)

set_api_key(os.environ["ELEVEN_API_KEY"])

language_model = {
    "Portuguese": "eleven_multilingual_v1",
    "English": "eleven_monolingual_v1",
}


class VoiceNotFoundError(Exception):
    """Exception raised when a specified voice does not exist."""

    def __init__(self, voice_name):
        self.voice_name = voice_name
        super().__init__(f"This voice does not exist: {self.voice_name}")


class VoiceGenerator:
    """
    A class for generating text-to-speech audio using
    the Eleven Labs API with various voice options.

    Args:
        voice_name (str): The name of the desired voice.

    Attributes:
        voice_list (list): List of available voices from the Eleven Labs API.
        voice_name (str): The name of the selected voice.
    """

    def __init__(self, voice_name):
        self.voice_list = voices()
        self.voice_name = voice_name

    def _voice_id(self):
        """
        Private method that retrieves the voice ID associated with the specified voice name.

        Returns:
            str: The voice ID for the selected voice.

        Raises:
            Exception: If the specified voice does not exist in the available voice list.
        """

        for voice in self.voice_list:
            if voice.name == self.voice_name:
                return voice.voice_id

        raise VoiceNotFoundError(self.voice_name)

    def text_to_speech(self, language: str, output_chatgpt: str):
        """
        Generates text-to-speech audio using the Eleven Labs API.

        Args:
            language (str): The language of the text.
            output_chatgpt (str): The text to be converted to speech.

        Returns:
            str: The temporary filename of the generated audio in MP3 format.

        Raises:
            requests.exceptions.RequestException: If an error occurs while making the API request.
        """

        chunk_size = 1024
        voice_id = self._voice_id()

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": os.environ["ELEVEN_API_KEY"],
        }

        data = {
            "text": output_chatgpt,
            "model_id": language_model[language],
            "voice_settings": {"stability": 0.7, "similarity_boost": 0.9},
        }

        response = requests.post(url, json=data, headers=headers, timeout=5)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
            file.flush()
            temp_filename = file.name

        return temp_filename
