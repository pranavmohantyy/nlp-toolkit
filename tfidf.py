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
    for tf_doc in tf:
        tfidf_doc = {word: tf_doc[word] * idf[word] for word in tf_doc}
        tfidf.append(tfidf_doc)
    return tfidf