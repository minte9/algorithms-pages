""" Word frequency
Example of using hash tables to count word frequency

In natural language processing (NLP), hash tables are used to count the frequency of words. 
The words are hashed, and their counts are stored as values.
"""

from icecream import ic

# Sample text
text = "This is a sample text document. It contains sample text for demonstration purposes."
words = text.split()

# Initialize a dictionary (hash table)
word_frequency = {}

# Count the frequency of each word
for word in words:

    # Remove punctuation and convert to lowercase
    word = word.strip(".,!?").lower()

    # Update the dictionary
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, frequency in word_frequency.items():
    ic(word, frequency)

"""
    ic| word: 'this', frequency: 1
    ic| word: 'is', frequency: 1
    ic| word: 'a', frequency: 1
    ic| word: 'sample', frequency: 2
    ic| word: 'text', frequency: 2
    ic| word: 'document', frequency: 1
    ic| word: 'it', frequency: 1
    ic| word: 'contains', frequency: 1
    ic| word: 'for', frequency: 1
    ic| word: 'demonstration', frequency: 1
    ic| word: 'purposes', frequency: 1
"""