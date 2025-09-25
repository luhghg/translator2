from googletrans import Translator

def translate_text(text: str, src: str = "auto", dest: str = "en") -> str:
    translator = Translator()
    try:
        result = translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"Ошибка перевода: {e}"
