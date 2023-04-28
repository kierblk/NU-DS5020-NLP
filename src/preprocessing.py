import nltk
from nltk.tokenize import word_tokenize, sent_tokenize


class Preprocessing:
    def __init__(self, dataset_path, disfluencies=None):
        self.dataset_path = dataset_path
        self.raw_text = ""
        self.sentences = []
        self.filtered_sentences = []
        if disfluencies is None:
            self.disfluencies = ["uh", "uhm"]
        else:
            self.disfluencies = disfluencies

    def read_data(self):
        with open(self.dataset_path, "r") as file:
            self.raw_text = file.read()

    def remove_punctuation(self):
        self.raw_text = self.raw_text.replace("'", "")

    def tokenize_sentences(self):
        self.sentences = sent_tokenize(self.raw_text)
        # Print Raw Data
        print("""
        PART 1
        ------
        
        Load and preprocess the dataset provided:
        - Tokenize the text, keeping only actual words while removing disfluencies such as “uh” 
        and “uhm”
        - Add special tokens to indicate the beginning of each sentence 
        
        """)
        print("\n------ Sampled Raw Data - START------\n")
        for i in range(5):
            print(self.sentences[i])
        print("\n------ END ------\n")

    def tokenize_words(self):
        self.filtered_sentences = [word_tokenize(sentence) for sentence in self.sentences]

    def contains_non_alpha_chars(self, token):
        for char in token:
            if not char.isalpha():
                return True
        return False

    def remove_disfluencies(self):
        for i, sentence in enumerate(self.filtered_sentences):
            self.filtered_sentences[i] = [
                token.strip("_") for token in sentence
                if token.lower() not in self.disfluencies
                and not self.contains_non_alpha_chars(token)
            ]

    def add_start_tokens(self, start_token):
        for sentence in self.filtered_sentences:
            sentence.insert(0, start_token)

        print("\n------ Sampled Processed Data - START------\n")
        for i in range(5):
            print(self.filtered_sentences[i])
        print("\n------ END ------\n")

    def preprocess(self, start_token="</s>"):
        nltk.download("punkt")
        self.read_data()
        self.remove_punctuation()
        self.tokenize_sentences()
        self.tokenize_words()
        self.remove_disfluencies()
        self.add_start_tokens(start_token)
