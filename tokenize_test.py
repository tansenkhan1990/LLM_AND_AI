# If you haven't installed NLTK, uncomment the next line:
# !pip install nltk

import nltk

# Download necessary NLTK data files (only need to run once)
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize, word_tokenize

# Sample text for tokenization
text = """
Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard. Dr. Adams won 1.5 million dollars!
"""

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}: {sentence}")

print("\n" + "-"*40 + "\n")

# Word Tokenization for each sentence
print("Word Tokenization (per sentence):")
for i, sentence in enumerate(sentences, 1):
    words = word_tokenize(sentence)
    print(f"Sentence {i} words: {words}")

# If you want to tokenize the whole text into words (not per sentence):
all_words = word_tokenize(text)
print("\nAll words in the text:")
print(all_words)
