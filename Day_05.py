"""Day 5 String Manipulation
==========================
1. Write a function to count the number of vowels in a given string
2. Given a list of words, concatenate them into a single string separated by spaces
3. Create a function to reverse a given string
4. Write a program that takes a string as input and counts the number of words in it
5. Given a string, write a function to removes all vowels from it and returns the resulting string
6. Write a Python program to find the length onf the longest word in a sentence
7. Create a function that takes a sentence as input and returns the sentence in reverse order
8. Given a list of names, count the number of names that start with a vowel
9. Write a function to remove all dulicate characters from a sentence
10. Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence

"""

# -------------------------------------------------------------------
# 1. Write a function to count the number of vowels in a given string
def count_vowels(string):
    count = 0
    for char in string:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count
count_vowels("This is a text for testing the function")

# -------------------------------------------------------------------
# 2. Given a list of words, concatenate them into a single string separated by spaces
def concatenate_words(words):
    return ' '.join(words)
concatenate_words(["This", "is", "a", "test"])

# -------------------------------------------------------------------
# 3. Create a function to reverse a given string
def reverse_string(string):
    return string[::-1] 
reverse_string(["Test", "another", "is", "This"])

# -------------------------------------------------------------------
# 4. Write a program that takes a string as input and counts the number of words in it

string = input("Enter a sentence: ")
def count_words(string):
    return len(string.split())
count_words(string)

# -------------------------------------------------------------------
# 5. Given a string, write a function to removes all vowels from it and returns the resulting string    
def remove_vowels(string):
    return ''.join([char for char in string if char not in 'aeiouAEIOU'])
remove_vowels("char for char in string iterates over each character in the variable") 

# -------------------------------------------------------------------
# 6. Write a Python program to find the length onf the longest word in a sentence
def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
find_longest_word("This is a test for the function to find the longest word")

# -------------------------------------------------------------------
# 7. Create a function that takes a sentence as input and returns the sentence in reverse order
sentence = input("Enter a long sentence: ")
def reverse_sentence(sentence):
    return ' '.join(reversed(sentence.split()))
reverse_sentence(sentence)

# -------------------------------------------------------------------
# 8. Given a list of names, count the number of names that start with a vowel

word_list = ['Mariah', 'Louise', 'Elvis', 'Carolina', 'Michael', 'Andres', 'Antony']
def count_starting_vowel(word_list):
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0

    for word in word_list:
        if word[0].lower() in vowels:
            count += 1
    return count
count_starting_vowel(word_list)


# -------------------------------------------------------------------
# 9. Write a function to remove all dulicate characters from a sentence
def remove_duplicates(sentence):
    return ''.join(set(sentence))
remove_duplicates("This is a test for the function to remove duplicates")

# -------------------------------------------------------------------
# 10. Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
def check_word(sentence, word):
    return word in sentence
check_word(sentence, word)

# -------------------------------------------------------------------
