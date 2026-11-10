import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

class TextClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = MultinomialNB()

    def train(self, corpus, labels):
        tfidf_matrix = self.vectorizer.fit_transform(corpus)
        self.model.fit(tfidf_matrix, labels)

    def predict(self, new_docs):
        tfidf_matrix = self.vectorizer.transform(new_docs)
        return self.model.predict(tfidf_matrix)
