"""Exercicio 15:
Crie uma função para determinar se uma sentença é ou não um pangrama."""

# using string constant to facilitate
from string import ascii_lowercase


def is_pangram(sentence: str):
    sentence = sentence.lower()  # converts input to lowercase

    # verifies if list containing all letters is in provided sentence
    for letter in ascii_lowercase:
        if letter not in sentence:
            return "Sentence is not a pangram"

    return "Sentence is a pangram"
