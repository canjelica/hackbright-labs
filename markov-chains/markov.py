"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()
    # text_string.replace(\n, " ")
    
    # print(text_string)
    return text_string


    # return open(file_path).read()



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    wordlist = text_string.split()

    # print(text_string)

    for i in range(len(wordlist) - 2):
        word_pairs = (wordlist[i], wordlist[i + 1])
        word_pairs_value = wordlist[i+2]
        # chains[word_pairs] = word_pairs_value
        # valueslist = list(word_pairs_value)

        
        followers = chains.get(word_pairs,[])
        followers.append(word_pairs_value)
        
        chains[word_pairs] = followers
    
    return chains
 



def make_text(chains):
    """Return text from chains."""
    import random

    words = []

    # chain_keys = chains.keys()
    # chain_values = chains.values()

    # for chain in chains:
    #     link = random.choice(chains[chain])
    #     print(link)

    key = choice(list(chains.keys()))
    
    values = chains[key]


    first_word = key[0]
    keyvalue = values[0]
    
    print(first_word)
    print(keyvalue)
    
    if first_word is not None: 
        words.append(first_word)
        words.append(keyvalue)
        first_word = keyvalue
    
              

    
    


        




    # your code goes here

    # return " ".join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)


text_string = open_and_read_file("green-eggs.txt")
chains = make_chains(text_string)