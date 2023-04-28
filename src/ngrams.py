import nltk


class NGrams:
    def __init__(self, preprocessed_data):
        self.preprocessed_data = preprocessed_data
        self.unigrams = []
        self.bigrams = []
        self.trigrams = []

    def generate_unigrams(self):
        for sentence in self.preprocessed_data:
            for token in sentence[1:]:  # Start from the second token
                self.unigrams.append(token)

    def generate_bigrams(self):
        for sentence in self.preprocessed_data:
            bigrams = list(nltk.bigrams(sentence[1:]))  # Start from the second token
            self.bigrams.extend(bigrams)

    def generate_trigrams(self):
        for sentence in self.preprocessed_data:
            trigrams = list(nltk.trigrams(sentence[1:]))  # Start from the second token
            self.trigrams.extend(trigrams)

    def generate_ngrams(self):
        self.generate_unigrams()
        self.generate_bigrams()
        self.generate_trigrams()
