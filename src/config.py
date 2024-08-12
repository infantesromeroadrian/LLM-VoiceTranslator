# config.py
import torch

CONFIG = {
    'DEVICE': "cuda" if torch.cuda.is_available() else "cpu",
    'SAMPLE_RATE': 16000,
    'CHANNELS': 1,
    'WHISPER_MODEL': "openai/whisper-large-v2",
    'M2M100_MODEL': "facebook/m2m100_1.2B",
    'SPEECHT5_MODEL': "microsoft/speecht5_tts",
    'SPEECHT5_VOCODER': "microsoft/speecht5_hifigan",
    'LANGUAGES': {
        'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de',
        'Italian': 'it', 'Portuguese': 'pt', 'Russian': 'ru', 'Chinese': 'zh',
        'Japanese': 'ja', 'Korean': 'ko'
    }
}