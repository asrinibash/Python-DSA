# Checking for Palindrome Using Extended Slicing Technique

str1="kidney"
str2="yendik"


def check_palindrome(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    
    if str1== str2[::-1]:
        print("TRUE")
    else:
        print("FALSE")
        
check_palindrome(str1,str2)