from preprocessing import Preprocessing
from ngrams import NGrams
from probability import Probability
from random import shuffle


def main():
    # Set the dataset path
    dataset_path = "../data/berkeley_restaurant_dataset.txt"

    # Create an instance of the Preprocessing class with the dataset path
    data = Preprocessing(dataset_path)

    # Preprocess the dataset
    data.preprocess()

    # Grab the preprocessed sentences to print them
    preprocessed_data = data.filtered_sentences

    # Create an instance of the NGrams class with the preprocessed data
    ngrams = NGrams(preprocessed_data)

    # Generate unigrams, bigrams, and trigrams
    ngrams.generate_ngrams()

    # Access the generated ngrams
    unigrams = ngrams.unigrams
    bigrams = ngrams.bigrams
    trigrams = ngrams.trigrams

    # For testing - Print some example ngrams
    # print("Unigrams:", unigrams[:10])
    # print("Bigrams:", bigrams[:10])
    # print("Trigrams:", trigrams[:10])

    # Print the requested statistics on word count, vocabulary size,
    # and total number of sentences
    ngrams.print_statistics()

    print("""

        PART 3
        ------

        Read the chapter on N-grams and generate figures 4.1 and 4.2 
        for bigram 
        counts. The figures do not have to be exact.

        """)
    print("------ Bigram Count Table - Figure 4.1 -------\n")
    ngrams.bigram_count_table()

    print("\n------ Bigram Probability Table - Figure 4.2 -------\n")
    ngrams.bigram_probability_table()

    print("""

        PART 4 & 5
        ------

        Calculate the joint probability for at least five sentences (with vocabulary in the dataset) using bigrams. 
        Repeat step 2 using trigrams. Observe if the estimates have changed. 

    """)
    print("\n------ Calculate bigram and trigram probabilities --------\n")

    probability = Probability(ngrams.bigrams, ngrams.trigrams)
    bigram_probs = probability.bigram_probabilities()
    trigram_probs = probability.trigram_probabilities()

    sentences = data.filtered_sentences

    shuffle(sentences)
    examples = []
    for sentence in sentences:
        if len(sentence[1:]) > 2:
            examples.append(sentence)

    for sentence in examples[:5]:
        if len(sentence[1:]) > 2:
            print(f"Sentence: {' '.join(sentence[1:])}")
            print(f"Bigram Probability: {bigram_probs[(sentence[1], sentence[2])]}")
            print(f"Trigram Probability: {trigram_probs[(sentence[1], sentence[2], sentence[3])]}")
            print()


if __name__ == "__main__":
    main()

