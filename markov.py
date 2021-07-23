"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):

    file = open(file_path)
    file_str = file.read()
    file.close()
    
    return file_str


def make_chains(text_string):

    chains = {}

    text_string = text_string.split()

    text_string.append(None)

    for i in range(len(text_string) - 2):
        key = (text_string[i], text_string[i + 1])
        value = text_string[i + 2]

        if key not in chains:
            chains[key] = []
        
        chains[key].append(value)
    
    return chains


def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return ' '.join(words)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

def make_random_text():
    return make_text(chains)