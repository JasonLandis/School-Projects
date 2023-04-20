import Regex

string = input("Enter a string: ")

# search the string for two or more consecutive vowels
# and print the result
Regex.stringSearch(string, r'[aeiou]{2,}')
