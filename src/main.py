from preprocessing import Preprocessing


def main():
    # Set the dataset path
    dataset_path = "../data/berkeley_restaurant_dataset.txt"

    # Create an instance of the Preprocessing class with the dataset path
    data = Preprocessing(dataset_path)

    # Preprocess the dataset
    data.preprocess()

    # Grab the preprocessed sentences to print them
    preprocessed_sentences = data.filtered_sentences
    for i in range(5):
        print(preprocessed_sentences[i])


if __name__ == "__main__":
    main()

