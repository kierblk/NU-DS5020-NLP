import random
import nltk
from collections import Counter
from tabulate import tabulate


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

        print("""
        PART 2
        ------

        - Count the words
        - Report the size of the vocabulary 
        - report the number of sentences in the dataset

        """)

        print(f"WORD COUNT - Total number of words in the dataset:"
              f" {word_count}")
        print(f"VOCAB SIZE - Total number of unique words in the dataset:"
              f" {vocab_size}")
        print(f"SENTENCE COUNT - Number of sentences in the dataset:"
              f" {sentence_count}")

    def bigram_count_table(self, num_words = 8):
        # Get a random set of unique words < -- Original goal
        # commented out to use the words from the mentioned text
        # unique_words = list(set(self.unigrams))
        # selected_words = random.sample(unique_words, num_words)
        selected_words = ['i', 'want', 'to', 'eat', 'chinese', 'food',
                          'lunch', 'spend']

        # Calculate bigram counts
        bigram_counts = Counter(self.bigrams)

        # Create a matrix with bigram counts
        matrix = []
        for w1 in selected_words:
            row = []
            for w2 in selected_words:
                row.append(bigram_counts[(w1, w2)])
            matrix.append(row)

        # Display the matrix in a tabular format
        headers = [''] + selected_words
        table = tabulate(
            matrix, headers = headers, showindex = selected_words,
            tablefmt = "grid", numalign = "right"
            )
        print(table)

    def bigram_probability_table(self, num_words = 8):
        # Get a random set of unique words < -- Original goal
        # commented out to use the words from the mentioned text
        # unique_words = list(set(self.unigrams))
        # selected_words = random.sample(unique_words, num_words)
        selected_words = ['i', 'want', 'to', 'eat', 'chinese', 'food',
                          'lunch', 'spend']

        # Calculate unigram counts
        unigram_counts = Counter(self.unigrams)

        # Calculate bigram counts
        bigram_counts = Counter(self.bigrams)

        # Create a matrix with bigram probabilities
        matrix = []
        for w1 in selected_words:
            row = []
            for w2 in selected_words:
                bigram_count = bigram_counts[(w1, w2)]
                unigram_count = unigram_counts[w1]
                probability = bigram_count / unigram_count if unigram_count > 0 else 0
                row.append(probability)
            matrix.append(row)

        # Display the matrix in a tabular format
        headers = [''] + selected_words
        table = tabulate(
            matrix, headers = headers, showindex = selected_words,
            tablefmt = "grid", floatfmt = ".4f", numalign = "right"
            )
        print(table)
