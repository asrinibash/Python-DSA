# Removing All Whitespace in a String


import re

def remove_whiteSpace(string):
    spaces=re.compile(r'\s+')
    count=re.sub(spaces,'',string)
    
    
    return count

print(remove_whiteSpace("Srini bash Achary"))