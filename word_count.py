sentence = input("Enter a sentence: ")
word = input("Enter a word to count: ")
words_in_sentence = sentence.split()
count = 0
for w in words_in_sentence:
    if w == word:
        count += 1
print("Number of occurrences of '{}' in the sentence: {}".format(word, count))
