import nltk
from nltk.corpus import reuters
from text_classifier import TextClassifier
from sklearn.metrics import accuracy_score

nltk.download('reuters')

class Benchmark:
    def __init__(self):
        self.corpus = reuters.sents()
        self.labels = [reuters.categories(fileid) for fileid in reuters.fileids()]
        self.classifier = TextClassifier()

    def run(self):
        train_docs, test_docs, train_labels, test_labels = train_test_split(self.corpus, self.labels, test_size=0.2)
        self.classifier.train([' '.join(doc) for doc in train_docs], train_labels)
        predictions = self.classifier.predict([' '.join(doc) for doc in test_docs])
        accuracy = accuracy_score(test_labels, predictions)
        print(f"Accuracy: {accuracy * 100:.2f}%")

if __name__ == '__main__':
    benchmark = Benchmark()
    benchmark.run()