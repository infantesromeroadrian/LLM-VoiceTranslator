# Interfaz

## GradioInterface

Proporciona una interfaz web interactiva utilizando Gradio.

### Métodos principales:
- `translate(audio: np.array, source_lang: str, target_lang: str) -> Tuple[str, np.array]`: 
  Método principal que maneja la entrada de audio y devuelve la traducción en texto y audio.

- `launch() -> None`: Inicia la interfaz web de Gradio.

### Componentes de la interfaz:
- Input Audio: Permite al usuario grabar o cargar un archivo de audio.
- Source Language: Menú desplegable para seleccionar el idioma de origen.
- Target Language: Menú desplegable para seleccionar el idioma de destino.
- Translated Text: Muestra el texto traducido.
- Translated Audio: Reproduce el audio traducido.