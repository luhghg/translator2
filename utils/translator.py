# файл для перевода текста через Google Translate
from googletrans import Translator

def translate_text(text: str, src: str = "auto", dest: str = "en") -> str:
    """
    Переводит текст с языка src на язык dest.
    
    :param text: текст для перевода
    :param src: исходный язык (по умолчанию "auto")
    :param dest: язык перевода (по умолчанию "en")
    :return: переведённый текст или сообщение об ошибке
    """
    translator = Translator()
    try:
        result = translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"Ошибка перевода: {e}"
