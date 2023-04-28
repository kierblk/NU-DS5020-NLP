from preprocessing import Preprocessing
from ngrams import NGrams


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

    # Print some example ngrams
    print("Unigrams:", unigrams[:10])
    print("Bigrams:", bigrams[:10])
    print("Trigrams:", trigrams[:10])


if __name__ == "__main__":
    main()

