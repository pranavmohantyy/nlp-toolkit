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
        return list(set(phrase_list))

    def _calculate_word_scores(self, phrases):
        word_frequency = {}
        word_degree = {}
        for phrase in phrases:
            words = phrase.split()
            degree = len(words) - 1
            for word in words:
                word_frequency[word] = word_frequency.get(word, 0) + 1
                word_degree[word] = word_degree.get(word, 0) + degree
        word_scores = {word: word_degree[word] / word_frequency[word] for word in word_frequency}
        return word_scores

    def extract_keywords(self, text):
        phrases = self._generate_candidate_keywords(text)
        word_scores = self._calculate_word_scores(phrases)
        sorted_keywords = sorted(word_scores.items(), key=lambda x: x[1], reverse=True)
        return [keyword for keyword, score in sorted_keywords]