# gradio_interface.py
import gradio as gr
import numpy as np
import soundfile as sf
from scipy import signal
import os
from src.features.voice_translator import VoiceTranslator
from src.config import CONFIG
from src.utils.logger import logger


class GradioInterface:
    def __init__(self):
        self.translator = VoiceTranslator()
        self.languages = CONFIG['LANGUAGES']
        logger.info("GradioInterface initialized")

    def resample_audio(self, audio, orig_sr, target_sr=CONFIG['SAMPLE_RATE']):
        logger.info(f"Resampling audio from {orig_sr} Hz to {target_sr} Hz")
        resampled = signal.resample(audio, int(len(audio) * target_sr / orig_sr))
        return resampled

    def translate(self, audio, source_lang, target_lang):
        try:
            if audio is None:
                logger.warning("No audio detected")
                return "No audio detected. Please try again.", None

            logger.info(f"Translating from {source_lang} to {target_lang}")

            orig_sr = audio[0]
            audio_data = audio[1]
            if len(audio_data.shape) > 1:
                audio_data = audio_data.mean(axis=1)
            if orig_sr != CONFIG['SAMPLE_RATE']:
                audio_data = self.resample_audio(audio_data, orig_sr)

            audio_data = audio_data / np.max(np.abs(audio_data))

            temp_file = "temp_input_audio.wav"
            sf.write(temp_file, audio_data, CONFIG['SAMPLE_RATE'])
            logger.info(f"Audio saved to {temp_file}")

            source_lang_code = self.languages[source_lang]
            target_lang_code = self.languages[target_lang]

            translated_text, audio_output = self.translator.translate_speech(temp_file, source_lang_code,
                                                                             target_lang_code)

            if translated_text is None or audio_output is None:
                return "Translation failed. Please try again.", None

            os.remove(temp_file)

            return translated_text, (CONFIG['SAMPLE_RATE'], audio_output)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}", exc_info=True)
            return f"An error occurred: {str(e)}", None

    def launch(self):
        iface = gr.Interface(
            fn=self.translate,
            inputs=[
                gr.Audio(type="numpy", label="Input Audio"),
                gr.Dropdown(list(self.languages.keys()), label="Source Language"),
                gr.Dropdown(list(self.languages.keys()), label="Target Language")
            ],
            outputs=[
                gr.Textbox(label="Translated Text"),
                gr.Audio(type="numpy", label="Translated Audio")
            ],
            title="Voice Translator",
            description="Translate speech from one language to another."
        )
        iface.launch()