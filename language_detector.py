import re
from collections import Counter

class LanguageDetector:
    def __init__(self):
        self.languages = {
            'english': {'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd'},
            'spanish': {'e', 'a', 'o', 's', 'n', 'r', 't', 'i', 'l', 'c'},
            'french': {'e', 'a', 'i', 's', 't', 'n', 'r', 'o', 'u', 'l'}
        }

    def _get_character_ngrams(self, text, n):
        text = re.sub(r'\W+', '', text.lower())
        return Counter(text[i:i+n] for i in range(len(text) - n + 1))

    def detect(self, text):
        n = 2
        text_ngrams = self._get_character_ngrams(text, n)
        scores = {lang: sum(text_ngrams[char] for char in chars) for lang, chars in self.languages.items()}
        return max(scores, key=scores.get)
