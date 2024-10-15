# OPEN ACCESS: https://www.hackerrank.com/challenges/pangrams/problem

def isPangram(pangrams):
    result = []
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    for sentence in pangrams:
        sentence_letters = set(sentence.lower())
        
        if alphabet.issubset(sentence_letters):
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)

