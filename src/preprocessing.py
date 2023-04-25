import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# read in the dataset
with open("../data/berkeley_restaurant_dataset.txt", "r") as file:
    raw_text = file.read()

# tokenizer
nltk.download("punkt")

# sentence tokenizer
sentences = sent_tokenize(raw_text)

# for testing
print("\n------ raw data - start------\n")
for i in range(5):
    print(sentences[i])
print("\n------ raw data - end------\n")

# provided disfluencies
disfluencies = ["uh", "uhm"]

# begin filtering individual sentences - create tokens from sentences then
# evaluate the token against the provided disfluenceies
filtered_sentences = []
for sentence in sentences:
    tokens = word_tokenize(sentence)
    filtered_tokens = [token for token in tokens if token.lower() not in disfluencies]
    filtered_sentences.append(filtered_tokens)

# add a start token
start_token = "</s>"
for tokens in filtered_sentences:
    tokens.insert(0, start_token)

# for testing
print("\n------ processed data - start------\n")
for i in range(5):
    print(filtered_sentences[i])
print("\n------ processed data - end------\n")
