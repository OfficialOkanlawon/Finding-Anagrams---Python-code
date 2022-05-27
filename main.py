# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from pyparsing import Word


def find_anagram(word, anagram):
    if sorted(anagram) == sorted(word):
        return True
    else:
        return False

firstWord = input("Enter the first word ")
secondWord = input("Enter the second word ")
check = find_anagram(firstWord, secondWord)
print(check)