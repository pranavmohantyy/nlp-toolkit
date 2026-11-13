import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class TextSummarizer:
    def __init__(self, n_sentences=3):
        self.n_sentences = n_sentences
        self.vectorizer = TfidfVectorizer()

    def summarize(self, text):
        sentences = text.split('. ')
        tfidf_matrix = self.vectorizer.fit_transform(sentences)
        sentence_scores = np.sum(tfidf_matrix, axis=1)
        ranked_sentences = np.argsort(sentence_scores.flatten())[::-1]
        selected_sentences = sorted(ranked_sentences[:self.n_sentences])
        summary = '. '.join([sentences[i] for i in selected_sentences])
        return summary