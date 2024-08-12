# utils.py
import logging
from colorama import Fore, Style, init

init(autoreset=True)

class ColoredLogger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)

    def info(self, msg, *args, **kwargs):
        super().info(f"{Fore.GREEN}{msg}{Style.RESET_ALL}", *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        super().warning(f"{Fore.YELLOW}{msg}{Style.RESET_ALL}", *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        super().error(f"{Fore.RED}{msg}{Style.RESET_ALL}", *args, **kwargs)

def setup_logger():
    logging.setLoggerClass(ColoredLogger)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logger()

def log_execution(func):
    def wrapper(*args, **kwargs):
        logger.info(f"{Fore.CYAN}Starting: {func.__name__}{Style.RESET_ALL}")
        result = func(*args, **kwargs)
        logger.info(f"{Fore.CYAN}Finished: {func.__name__}{Style.RESET_ALL}")
        return result
    return wrapper