import string

def is_palindrome(s1):
    if s1[::-1] == s1:
       return "It's a palindrome!"
    else:
        return "It is not a palindrome :-("