# voice_translator.py
from src.features.audio_recorder import AudioRecorder
from src.models.speech_recognizer import SpeechRecognizer
from src.models.translator import Translator
from src.models.text_to_speech import TextToSpeech
from src.utils import logger, log_execution

class VoiceTranslator:
    def __init__(self):
        self.recorder = AudioRecorder()
        self.recognizer = SpeechRecognizer()
        self.translator = Translator()
        self.tts = TextToSpeech()

    @log_execution
    def translate_speech(self, audio_file, source_lang, target_lang):
        text = self.recognizer.recognize(audio_file, language=source_lang)
        logger.info(f"Recognized text: {text}")

        if not text.strip():
            logger.warning("No speech detected. Please try again.")
            return None, None

        translated_text = self.translator.translate(text, source_lang, target_lang)
        logger.info(f"Translated text: {translated_text}")

        audio_output = self.tts.synthesize(translated_text)
        audio_output_slowed = self.tts.adjust_speed(audio_output)
        return translated_text, audio_output_slowed