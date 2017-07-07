# Paste your function heredef print_without_vowel(s):

def print_without_vowels(s):
    ''' This function takes in a string, removes the vowels and return a string without      vowels'''
    vowel= 'aAeEiIoOuU'
    string_without_vowel = ''
    for ii in s:
        if ii not in vowel:
            string_without_vowel +=ii
    print(string_without_vowel)

