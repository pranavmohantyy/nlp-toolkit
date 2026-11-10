import numpy as np
from collections import Counter
from math import log

def compute_tf(corpus):
    tf = []
    for doc in corpus:
        word_count = Counter(doc)
        total_words = len(doc)
        tf_doc = {word: count / total_words for word, count in word_count.items()}
        tf.append(tf_doc)
    return tf

def compute_idf(corpus):
    n_docs = len(corpus)
    idf = {}
    for doc in corpus:
        for word in set(doc):
            idf[word] = idf.get(word, 0) + 1
    for word, count in idf.items():
        idf[word] = log(n_docs / count) + 1
    return idf

def compute_tfidf(corpus):
    tf = compute_tf(corpus)
    idf = compute_idf(corpus)
    tfidf = []
    for doc_tf in tf:
        tfidf_doc = {word: tf_val * idf[word] for word, tf_val in doc_tf.items()}
        tfidf.append(tfidf_doc)
    return tfidf

def cosine_similarity(vec_a, vec_b):
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = sum(a ** 2 for a in vec_a) ** 0.5
    norm_b = sum(b ** 2 for b in vec_b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_product / (norm_a * norm_b)