# Modelos

## SpeechRecognizer

Utiliza el modelo Whisper de OpenAI para el reconocimiento de voz.

### Métodos principales:
- `recognize(audio_file: str) -> str`: Transcribe el audio del archivo proporcionado.

## Translator

Utiliza el modelo M2M100 de Facebook para la traducción de texto.

### Métodos principales:
- `translate(text: str, source_lang: str, target_lang: str) -> str`: Traduce el texto del idioma de origen al idioma de destino.

## TextToSpeech

Utiliza el modelo SpeechT5 de Microsoft para la síntesis de voz.

### Métodos principales:
- `synthesize(text: str) -> np.array`: Convierte el texto en un array de audio.
- `adjust_speed(audio: np.array, speed_factor: float = 0.8) -> np.array`: Ajusta la velocidad del audio.