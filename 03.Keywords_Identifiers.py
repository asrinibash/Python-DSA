# Keywords in Python 

# -> Python is case sensitive like any other language means there is difference between upper-case and lower-case

import keyword

print(keyword.kwlist)

# Currently Python has 35 keywords
print(len(['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']))




# Identifiers
#  python identifier is a name used to identify the variable, class, function, module or other objects

# Rules:
# can only start with alphabet or '_'
# followed by 0 or more letters, _ and digits -> not special characters
# keywords cannot used as identifier