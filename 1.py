from googletrans import Translator

translator = Translator()

translated = ('Start', 'Stop', 'Reset')

translator.translate(translated, dest = 'tl')