"""
Create a function that takes a sentence and prints the sentence without duplicated word
"""

def sentence_without_duplicate(sentence):
    words = sentence.split()
    i = 0
    while i <len(words):
        count = words.count(words[i])
        if count > 1:
            for _ in  range(count-1):
                words.remove(words[i])
        i+=1
    sentence = ' '.join(words)
    return sentence


print(sentence_without_duplicate("Every Every cloud has a a silver silver silver silver lining lining"))