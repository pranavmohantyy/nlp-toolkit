class Rake:
    def __init__(self, stopwords):
        self.stopwords = stopwords

    def _generate_candidate_keywords(self, text):
        sentences = text.split('. ')
        phrase_list = []
        for sentence in sentences:
            words = sentence.split()
            phrase = []
            for word in words:
                if word not in self.stopwords:
                    phrase.append(word)
                elif phrase:
                    phrase_list.append(' '.join(phrase))
                    phrase = []
            if phrase:
                phrase_list.append(' '.join(phrase))
        return phrase_list

    def extract_keywords(self, text):
        candidate_keywords = self._generate_candidate_keywords(text)
        return candidate_keywords