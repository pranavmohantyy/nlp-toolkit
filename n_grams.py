from collections import Counter

def generate_ngrams(corpus, n):
    ngrams = []
    for doc in corpus:
        doc_ngrams = zip(*[doc[i:] for i in range(n)])
        ngrams.extend(doc_ngrams)
    return ngrams


def compute_frequencies(ngrams):
    return Counter(ngrams)


def generate_ngram_frequencies(corpus):
    unigram_freq = compute_frequencies(generate_ngrams(corpus, 1))
    bigram_freq = compute_frequencies(generate_ngrams(corpus, 2))
    trigram_freq = compute_frequencies(generate_ngrams(corpus, 3))
    return unigram_freq, bigram_freq, trigram_freq