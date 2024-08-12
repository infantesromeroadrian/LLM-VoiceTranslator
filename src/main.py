import torch
from src.interface.gradio_interface import GradioInterface
from src.utils.logger import logger


def main():
    # Liberar memoria de la GPU si está disponible
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    logger.info("Starting Voice Translator application")

    # Iniciar la interfaz de Gradio
    interface = GradioInterface()
    interface.launch()


if __name__ == "__main__":
    main()