import sys
from brute_force import tokenize_input, output


def extract_n_gram(words, idx, n):
    end_idx = idx + n
    n_gram = words[idx:end_idx] # O(n) - tamanho do n grama
    return tuple(n_gram)

def count_n_grams(words, n, frequency):
    for idx, _ in enumerate(words):
        n_gram = extract_n_gram(words, idx, n)
        if (len(n_gram) >= n):
            if (n_gram in frequency):
                frequency[n_gram] +=1
            else:
                frequency[n_gram] = 1

def main():    
    file_name = sys.argv[1]
    n = int(sys.argv[2])

    with open(file_name) as point:
        frequency = {}
        for line in point:
            words = tokenize_input(line)
            count_n_grams(words, n, frequency)
    output(frequency)

"""
Otimizações desta versão:

1. Leitura linha a linha do arquivo de entrada. Lida com arquivos de texto
potencialmente muito grandes que, na implementação anterior, poderiam causar
uma sobrecarga na RAM.

Otimizações desejáveis:

1. O tamanho do dicionário de frequência pode ser tão grande quanto o vocabulário
português quando n=1. É difícil mensurar como o tamanho do dicionário varia
conforme a caridanilidade do n-grama é alterada, mas seria interessante carregar porções
do dicionário na memória, dinamicamente. Talvez fazendo um tradeoff entre cpu e memoria
ao armazenar, em disco, chunks do dicionario e carrega-los em memoria somente 
quando necessário. Algo similar a divisão e conquista. Não cheguei a implementar algo do tipo.
"""


if __name__ == '__main__':
    main()