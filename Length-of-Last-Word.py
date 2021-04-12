def lengthOfLastWord(sentence):
    words = sentence.split()
    if words:
        return len(words[-1])
    return 0

print(lengthOfLastWord("Hello World"))