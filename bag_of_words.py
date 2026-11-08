def build_vocabulary(corpus):
    vocab = set()
    for doc in corpus:
        for word in doc:
            vocab.add(word)
    return list(vocab)

def vectorize_documents(corpus, vocab):
    vectors = []
    for doc in corpus:
        vector = [0] * len(vocab)
        for word in doc:
            if word in vocab:
                index = vocab.index(word)
                vector[index] += 1
        vectors.append(vector)
    return vectors