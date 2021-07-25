import sys
import string

from collections import Counter
from nltk.util import ngrams

def preprocess_input(text): # O(n)
    clean_input = text.lower().replace(string.punctuation, '')
    return clean_input.split(' ') # O(n)

def output(frequency_dict):
    for k, v in frequency_dict.most_common():
        frequency = v
        n_gram = ' '.join(k)
        print(f'{frequency} - {n_gram}')


def main():    
    
    file_name = sys.argv[1]
    n = int(sys.argv[2])

    frequency = Counter()
    with open(file_name) as point:
        for line in point.read().splitlines():
            words = preprocess_input(line)
            line_ngrams = ngrams(words, n)
            for ngram in line_ngrams:
                frequency[ngram] += 1
    output(frequency)

if __name__ == '__main__':
    main()