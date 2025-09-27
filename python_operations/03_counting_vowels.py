# Counting Vowels in a given string

def count_vowel(string):
    vowels=['a','e','i','o','u']
    count=0
    
    for i in string:
        if i in vowels:
            count+=1
            
    return count
    
print(count_vowel("Srinibash"))