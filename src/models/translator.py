# translator.py
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from ..config import CONFIG
from ..utils import logger, log_execution

class Translator:
    def __init__(self):
        logger.info("Initializing M2M100 translation model")
        self.model = M2M100ForConditionalGeneration.from_pretrained(CONFIG['M2M100_MODEL'])
        self.tokenizer = M2M100Tokenizer.from_pretrained(CONFIG['M2M100_MODEL'])

    @log_execution
    def translate(self, text, source_lang, target_lang):
        logger.info(f"Translating from {source_lang} to {target_lang}")
        self.tokenizer.src_lang = source_lang
        encoded_text = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        generated_tokens = self.model.generate(
            **encoded_text,
            forced_bos_token_id=self.tokenizer.get_lang_id(target_lang),
            max_length=200,
            num_beams=5,
            length_penalty=0.8,
            no_repeat_ngram_size=3
        )
        translated = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return self.post_process_translation(translated)

    def post_process_translation(self, text):
        sentences = text.split('.')
        unique_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence and sentence not in unique_sentences:
                sentence = sentence.capitalize()
                if not sentence.endswith(('?', '!', '.')):
                    sentence += '.'
                unique_sentences.append(sentence)
        return ' '.join(unique_sentences)