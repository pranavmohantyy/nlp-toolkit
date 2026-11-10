import numpy as np
from collections import defaultdict

class Word2Vec:
    def __init__(self, corpus, window_size=2, embedding_dim=100):
        self.corpus = corpus
        self.window_size = window_size
        self.embedding_dim = embedding_dim
        self.word_vectors = {}
        self.vocab = self.build_vocab()
        self.initialize_vectors()

    def build_vocab(self):
        vocab = set()
        for doc in self.corpus:
            vocab.update(doc)
        return list(vocab)

    def initialize_vectors(self):
        for word in self.vocab:
            self.word_vectors[word] = np.random.rand(self.embedding_dim)

    def train(self, epochs=100):
        for _ in range(epochs):
            for doc in self.corpus:
                for idx, word in enumerate(doc):
                    start = max(0, idx - self.window_size)
                    end = min(len(doc), idx + self.window_size + 1)
                    context = [doc[i] for i in range(start, end) if i != idx]
                    self.update_vectors(word, context)

    def update_vectors(self, target_word, context_words):
        target_vector = self.word_vectors[target_word]
        for context_word in context_words:
            context_vector = self.word_vectors[context_word]
            self.word_vectors[target_word] += context_vector
            self.word_vectors[context_word] += target_vector

    def get_similar_words(self, word, top_n=5):
        target_vector = self.word_vectors[word]
        similarities = defaultdict(float)
        for other_word, vector in self.word_vectors.items():
            if other_word != word:
                similarity = np.dot(target_vector, vector) / (np.linalg.norm(target_vector) * np.linalg.norm(vector))
                similarities[other_word] = similarity
        return sorted(similarities, key=similarities.get, reverse=True)[:top_n]

# Sample usage:
# corpus = [['i', 'love', 'machine', 'learning'], ['machine', 'learning', 'is', 'fun']]
# model = Word2Vec(corpus)
# model.train()
# print(model.get_similar_words('machine'))