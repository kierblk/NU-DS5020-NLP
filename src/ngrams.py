import nltk

import nltk
from collections import Counter

class NGrams:
    def __init__(self, preprocessed_data):
        self.preprocessed_data = preprocessed_data
        self.unigrams = []
        self.bigrams = []
        self.trigrams = []

    def generate_unigrams(self):
        for sentence in self.preprocessed_data:
            for token in sentence[1:]:
                self.unigrams.append(token)

    def generate_bigrams(self):
        for sentence in self.preprocessed_data:
            bigrams = list(nltk.bigrams(sentence[1:]))
            self.bigrams.extend(bigrams)

    def generate_trigrams(self):
        for sentence in self.preprocessed_data:
            trigrams = list(nltk.trigrams(sentence[1:]))
            self.trigrams.extend(trigrams)

    def generate_ngrams(self):
        self.generate_unigrams()
        self.generate_bigrams()
        self.generate_trigrams()

    def count_words(self):
        return len(self.unigrams)

    def count_vocabulary(self):
        return len(set(self.unigrams))

    def count_sentences(self):
        return len(self.preprocessed_data)

    def print_statistics(self):
        word_count = self.count_words()
        vocab_size = self.count_vocabulary()
        sentence_count = self.count_sentences()

        print(f"WORD COUNT - Total number of words in the dataset:"
              f" {word_count}")
        print(f"VOCAB SIZE - Total number of unique words in the dataset:"
              f" {vocab_size}")
        print(f"SENTENCE COUNT - Number of sentences in the dataset:"
              f" {sentence_count}")
