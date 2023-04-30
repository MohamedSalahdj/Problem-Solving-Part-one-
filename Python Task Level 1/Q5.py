"""
Create a function that takes a sentence and prints how many words in the sentence (do not count the
spaces)
"""

#first way
def count_words_in_the_sentence(sentence):
    words = sentence.split()
    return len(words)

print(count_words_in_the_sentence("When in Rome do as the Romans do"))

#second way
def count_words_in_the_sentence_2(sentence):
    space = ' '
    # count = 0
    words_of_the_sentence = []
    word=''
    for letter in sentence:
        if letter == space:
            words_of_the_sentence.append(word)
            word=''
            continue
        word+=letter
    words_of_the_sentence.append(word)
    return words_of_the_sentence

print(count_words_in_the_sentence_2("When in Rome do as the Romans do"))