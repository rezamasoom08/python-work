import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    if forwards == backwards:
        return "This is a palindrome"
    else:
        return "Not a palindrome"
    
str = input("Enter a string: ")
print(is_palindrome(str))