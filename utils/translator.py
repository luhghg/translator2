from googletrans import Translator

# створюємо один екземпляр перекладача
translator = Translator()

async def translate_text(text: str, src: str = "auto", dest: str = "en") -> str:
    """
    Асинхронний переклад тексту з googletrans.
    src – мова оригіналу (або 'auto')
    dest – мова перекладу
    """
    try:
        # 👇 у нових версіях translate() – асинхронна функція
        result = await translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"Ошибка перевода: {e}"
