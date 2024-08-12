# text_to_speech.py
import torch
import numpy as np
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from ..config import CONFIG
from ..utils import logger, log_execution

class TextToSpeech:
    def __init__(self):
        logger.info("Initializing SpeechT5 text-to-speech model")
        self.processor = SpeechT5Processor.from_pretrained(CONFIG['SPEECHT5_MODEL'])
        self.model = SpeechT5ForTextToSpeech.from_pretrained(CONFIG['SPEECHT5_MODEL'])
        self.vocoder = SpeechT5HifiGan.from_pretrained(CONFIG['SPEECHT5_VOCODER'])
        self.speaker_embeddings = torch.randn(1, 512)

    @log_execution
    def synthesize(self, text):
        logger.info("Synthesizing speech")
        inputs = self.processor(text=text, return_tensors="pt")
        speech = self.model.generate_speech(inputs["input_ids"], self.speaker_embeddings, vocoder=self.vocoder)
        return speech.numpy()

    def adjust_speed(self, audio, speed_factor=0.8):
        return np.interp(
            np.arange(0, len(audio), speed_factor),
            np.arange(0, len(audio)),
            audio
        ).astype(audio.dtype)