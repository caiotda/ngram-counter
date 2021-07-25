import sys

def tokenize_input(text): # O(n)
    clean_input = text.replace('\n', ' ') # O(n) - Boyer-Moore
    return clean_input.split(' ') # O(n)

def sort_dictionary(frequency, descending=True): # O(n)
    return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=descending))

def output(frequency_dict):
    sorted_dict = sort_dictionary(frequency_dict) # O(n)
    for k, v in sorted_dict.items():
        frequency = v
        n_gram = ' '.join(k)
        print(f'{frequency} - {n_gram}')

def extract_n_gram(words, idx, n):
    end_idx = idx + n
    n_gram = words[idx:end_idx] # O(n) - tamanho do n grama
    n_gram = [word.lower() for word in n_gram]
    return tuple(n_gram)

def count_n_grams(words, n):
    frequency = {}
    for idx, _ in enumerate(words):
        n_gram = extract_n_gram(words, idx, n)
        if (len(n_gram) >= n):
            if (n_gram in frequency):
                frequency[n_gram] +=1
            else:
                frequency[n_gram] = 1
    return frequency

def main():    
    file_name = sys.argv[1]
    n = int(sys.argv[2])

    file = open(file_name, 'r')
    text = file.read()

    words = tokenize_input(text)
    frequency = count_n_grams(words, n)

    output(frequency)
    file.close()

if __name__ == '__main__':
    main()