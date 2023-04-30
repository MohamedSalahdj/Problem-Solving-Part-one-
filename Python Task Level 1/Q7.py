"""
Create a function takes a sentence and a word and prints how many time the word used in the sentence

"""



def times_of_the_word(sentence, word):
    words = sentence.split()
    count_of_word = words.count(word)
    return count_of_word

print(times_of_the_word("Do the good and good come to you",'good'))