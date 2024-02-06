# AP Computer Science Principles 1.1.9 Project
# @authors Nathan Gillespie, Ila Gowda, Chloe Han
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Example
if __name__ == '__main__':
    install('Translate')

from translate import Translator

# Dictionary mapping language names (both full and abbreviated) to language codes
language_names_to_codes = {
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
    'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
    'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chinese': 'zh-CN', 'chinese (simplified)': 'zh-CN',
    'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs',
    'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et',
    'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl',
    'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
    'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn',
    'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga',
    'italian': 'it', 'japanese': 'ja', 'javanese': 'jv', 'kannada': 'kn', 'kazakh': 'kk',
    'khmer': 'km', 'kinyarwanda': 'rw', 'korean': 'ko', 'kurdish': 'ku', 'kyrgyz': 'ky',
    'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb',
    'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt',
    'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne',
    'norwegian': 'no', 'nyanja (chichewa)': 'ny', 'odia (oriya)': 'or', 'pashto': 'ps',
    'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro',
    'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st',
    'shona': 'sn', 'sindhi': 'sd', 'sinhala (sinhalese)': 'si', 'slovak': 'sk', 'slovenian': 'sl',
    'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv',
    'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr',
    'turkmen': 'tk', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz',
    'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu',
    'af': 'af', 'sq': 'sq', 'am': 'am', 'ar': 'ar', 'hy': 'hy',
    'az': 'az', 'eu': 'eu', 'be': 'be', 'bn': 'bn', 'bs': 'bs',
    'bg': 'bg', 'ca': 'ca', 'ceb': 'ceb', 'zh': 'zh-CN', 'zh-cn': 'zh-CN',
    'zh-tw': 'zh-TW', 'co': 'co', 'hr': 'hr', 'cs': 'cs',
    'da': 'da', 'nl': 'nl', 'en': 'en', 'eo': 'eo', 'et': 'et',
    'tl': 'tl', 'fi': 'fi', 'fr': 'fr', 'fy': 'fy', 'gl': 'gl',
    'ka': 'ka', 'de': 'de', 'el': 'el', 'gu': 'gu', 'ht': 'ht',
    'ha': 'ha', 'haw': 'haw', 'he': 'he', 'hi': 'hi', 'hmn': 'hmn',
    'hu': 'hu', 'is': 'is', 'ig': 'ig', 'id': 'id', 'ga': 'ga',
    'it': 'it', 'ja': 'ja', 'jv': 'jv', 'kn': 'kn', 'kk': 'kk',
    'km': 'km', 'rw': 'rw', 'ko': 'ko', 'ku': 'ku', 'ky': 'ky',
    'lo': 'lo', 'la': 'la', 'lv': 'lv', 'lt': 'lt', 'lb': 'lb',
    'mk': 'mk', 'mg': 'mg', 'ms': 'ms', 'ml': 'ml', 'mt': 'mt',
    'mi': 'mi', 'mr': 'mr', 'mn': 'mn', 'my': 'my', 'ne': 'ne',
    'no': 'no', 'ny': 'ny', 'or': 'or', 'ps': 'ps',
    'fa': 'fa', 'pl': 'pl', 'pt': 'pt', 'pa': 'pa', 'ro': 'ro',
    'ru': 'ru', 'sm': 'sm', 'gd': 'gd', 'sr': 'sr', 'st': 'st',
    'sn': 'sn', 'sd': 'sd', 'si': 'si', 'sk': 'sk', 'sl': 'sl',
    'so': 'so', 'es': 'es', 'su': 'su', 'sw': 'sw', 'sv': 'sv',
    'tg': 'tg', 'ta': 'ta', 'tt': 'tt', 'te': 'te', 'th': 'th', 'tr': 'tr',
    'tk': 'tk', 'uk': 'uk', 'ur': 'ur', 'ug': 'ug', 'uz': 'uz',
    'vi': 'vi', 'cy': 'cy', 'xh': 'xh', 'yi': 'yi', 'yo': 'yo', 'zu': 'zu'
}

def get_language_code(language_name):
    language_name = language_name.lower()
    return language_names_to_codes.get(language_name)

input_text = input("What phrase would you like to translate? --> ")
language_name = input("Enter the language name --> ")

language_code = get_language_code(language_name)
if language_code:
    translator = Translator(to_lang=f'{language_code}')
    translated_text = translator.translate(input_text)

    print(f"The {language_name} translation of '{input_text}' is '{translated_text}'")
else:
    print(f"Language '{language_name}' not found.")
