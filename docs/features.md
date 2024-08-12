# Características

## AudioRecorder

Graba audio del micrófono del usuario.

### Métodos principales:
- `record(duration: float) -> np.array`: Graba audio durante la duración especificada.
- `save_audio(recording: np.array, filename: str) -> None`: Guarda la grabación en un archivo.

## VoiceTranslator

Coordina el proceso de traducción de voz a voz.

### Métodos principales:
- `translate_speech(audio_file: str, source_lang: str, target_lang: str) -> Tuple[str, np.array]`: 
  Traduce el audio de entrada y devuelve el texto traducido y el audio sintetizado.