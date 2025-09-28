# Find the First Non-Repeating Character

def find_first_non_repeating_character(s):
    for i in s:
        if s.count(i)==1:
            return i
        
    return None
    
print(find_first_non_repeating_character("srinibash"))