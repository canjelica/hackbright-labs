# put your code here.
"""Write a program, wordcount.py, that opens a file 
and counts how many times each space-separated word 
occurs in that file. Your program should then print 
those counts to the screen."""


# put each word into a tuple

# count occurrene of each word

# add each word as keyword in dictionary

# print each dictionary value

import sys

def tokenize(filename):
    """Return list of words from file"""

    tokens = []

    with open(filename) as text_file:
        for line in text_file:
            line = line.strip()
            words = line.split(" ") 

            for word in words:
                word = word.strip("'\",.!@#$%^&*();:_")
                word = word.lower()
                tokens.extend(words)
 
    return tokens

def count_words(wordlist):
    word_dict = {}

    for word in wordlist:
        word_dict[word] = word_dict.get(word, 0) + 1
    
    return word_dict


def print_words(word_dict):
    for word, count in word_dict.items():
        print(word, count)




    
    # dictionary to capture
    # adding each list item to dict
    
    
wordlist = tokenize("test.txt")
word_dict = count_words(wordlist)




   






