# NLP Toolkit

This is a collection of NLP utilities implemented from scratch, including tokenization, TF-IDF, word vectors, and text classification.

## Features
- Tokenization
- TF-IDF computation
- Word embeddings
- Text classification
- Language detection
- Named entity recognition
- Sentiment analysis
- Text summarization

## Usage Examples

### Tokenization
```python
from tokenizer import word_tokenize
text = "This is a sample text."
tokens = word_tokenize(text)
print(tokens)  # Output: ['this', 'is', 'a', 'sample', 'text']
```

### Text Classification
```python
from text_classifier import TextClassifier
classifier = TextClassifier()
corpus = ["I love programming.", "I hate bugs."]
labels = [1, 0]
classifier.train(corpus, labels)
new_docs = ["I enjoy coding."]
predictions = classifier.predict(new_docs)
print(predictions)  # Output: [1]
```

### Comparison with NLTK/spaCy
- **Tokenization**: The `tokenizer` module provides a simple tokenization method, similar to NLTK's `word_tokenize` function but custom-built.
- **Text Classification**: Our `TextClassifier` uses a Naive Bayes approach, while NLTK and spaCy offer more complex models and pre-trained classifiers.
- **Named Entity Recognition**: The `NamedEntityRecognizer` can extract names directly, while NLTK and spaCy provide extensive pre-trained models with greater accuracy.

## Installation
Clone the repository and use it directly in your Python projects.

## Requirements
- Python 3.x
- NumPy
- scikit-learn

## License
MIT License