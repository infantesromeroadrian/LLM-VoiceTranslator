# speech_recognizer.py
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import soundfile as sf
from ..config import CONFIG
from ..utils import logger, log_execution

class SpeechRecognizer:
    def __init__(self):
        logger.info(f"Initializing Whisper model on {CONFIG['DEVICE']}")
        self.processor = WhisperProcessor.from_pretrained(CONFIG['WHISPER_MODEL'])
        self.model = WhisperForConditionalGeneration.from_pretrained(CONFIG['WHISPER_MODEL']).to(CONFIG['DEVICE'])

    @log_execution
    def recognize(self, audio_file, language):
        logger.info(f"Recognizing speech in {language}")
        audio_input, sample_rate = sf.read(audio_file)
        input_features = self.processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_features.to(CONFIG['DEVICE'])
        forced_decoder_ids = self.processor.get_decoder_prompt_ids(language=language, task="transcribe")
        predicted_ids = self.model.generate(input_features, forced_decoder_ids=forced_decoder_ids)
        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)
        return transcription[0]