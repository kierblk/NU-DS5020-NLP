import nltk
from collections import defaultdict, Counter


class Probability:
    def __init__(self, bigrams, trigrams):
        self.bigrams = bigrams
        self.trigrams = trigrams

    def count_bigrams(self):
        bigram_counts = defaultdict(Counter)
        for bigram in self.bigrams:
            bigram_counts[bigram[0]][bigram[1]] += 1

        return bigram_counts

    def bigram_probabilities(self):
        bigram_counts = self.count_bigrams()

        bigram_probs = {}
        for first_word in bigram_counts:
            total_count = sum(bigram_counts[first_word].values())
            for second_word in bigram_counts[first_word]:
                bigram_probs[(first_word, second_word)] = bigram_counts[first_word][second_word] / total_count

        return bigram_probs

    def count_trigrams(self):
        trigram_counts = defaultdict(Counter)
        for trigram in self.trigrams:
            trigram_counts[(trigram[0], trigram[1])][trigram[2]] += 1

        return trigram_counts

    def trigram_probabilities(self):
        bigram_counts = self.count_bigrams()
        trigram_counts = self.count_trigrams()

        trigram_probs = {}
        for bigram in trigram_counts:
            for third_word in trigram_counts[bigram]:
                trigram_probs[bigram + (third_word,)] = trigram_counts[bigram][third_word] / bigram_counts[bigram[0]][bigram[1]]

        return trigram_probs