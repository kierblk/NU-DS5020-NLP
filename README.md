# Northeastern University, Spring 2023: DS 5020
## Simple Language Model using N-grams

Natural Language Processing (NLP) is a field of data science/AI that involves analyzing text and language data. This assignment aims to create a simple language model and gain insights into the application of probability to text data. The main objective is to load and tokenize the Berkeley Restaurant dataset, introduced in the “Speech and Language Processing'' book by Jurafsky. The following are the main steps involved in the assignment:

## Steps

- [x] Load and preprocess the dataset provided. Tokenize the text and keep 
   only actual words while removing disfluencies such as “uh” and “uhm”. Add special tokens to indicate the beginning of each sentence (e.g., `</s>`).
- [x] Count the words and report the size of the vocabulary. Also, report the 
  number of sentences in the dataset.
- [x] Read the chapter on N-grams and generate figures 4.1 and 4.2 for bigram 
  counts. The figures do not have to be exact. 
- [x] Calculate the joint probability for at least five sentences (with 
  vocabulary in the dataset) using bigrams. 
- [x] Repeat step 2 using trigrams. Observe if the estimates have changed. 
- [x] Submit the code or pdf of the program and output. The program should be 
  able to run.

## Tools

Python packages such as nltk will be used to accomplish this task. The N-gram model will be used to build the language model, and the joint probability will be calculated using the counts.

## Submission

The final submission will include the code or pdf of the program and output. The program should be able to run without any errors. Failing to submit a program that runs will result in no credit being assigned.