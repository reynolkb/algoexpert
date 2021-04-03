alphabet = 'abcdefghijklmnopqrstuvwxyz'
sentence = 'The five boxing wizards jump quickly'

def ispangram(sentence):
    sentence = sentence.lower()

    for letter in alphabet:
        if letter not in sentence:
            return False
    return True

print(ispangram(sentence))