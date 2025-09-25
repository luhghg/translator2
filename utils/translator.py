from googletrans import Translator

def translate_text(text: str, src: str = "auto", dest: str = "en") -> str:
    translator = Translator()
    result = translator.translate(text, src=src, dest=dest)
    return result.text
