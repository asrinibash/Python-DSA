# Adding Two List Elements Together


def string_anagram(str1,str2):
    str1=list(str1.upper())
    str2=list(str2.upper())
    
    str1.sort(), str2.sort()
    
    if str1==str2:
        print("True")
    else:
        print("False")
        
        
str1="Srinibash"
str2="hsabinirs"

string_anagram(str1,str2)