# audio_recorder.py
import sounddevice as sd
import soundfile as sf
from ..config import CONFIG
from ..utils import logger, log_execution

class AudioRecorder:
    def __init__(self):
        self.rate = CONFIG['SAMPLE_RATE']
        self.channels = CONFIG['CHANNELS']

    @log_execution
    def record(self, duration):
        logger.info(f"Recording for {duration} seconds...")
        recording = sd.rec(int(duration * self.rate), samplerate=self.rate, channels=self.channels)
        sd.wait()
        logger.info("Recording finished")
        return recording

    def save_audio(self, recording, filename):
        sf.write(filename, recording, self.rate)
        logger.info(f"Audio saved as '{filename}'")