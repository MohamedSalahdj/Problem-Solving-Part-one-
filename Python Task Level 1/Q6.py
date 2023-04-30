"""
Create a function that takes a sentence and word and remove the word from the sentence
"""

def remove_word_from_sentence(sentence, word):
    words = sentence.split()
    count_of_word = words.count(word)
    for _ in range(count_of_word):
        words.remove(word)
    sentence = ' '.join(words)
    return sentence


print(remove_word_from_sentence("What goes around comes around",'around'))