# Strings are sequence of characters
# in python specifically, strings are sequence of unicode characters

# before we have ascii character, but as we adding more countries languages characters.. the ascii which is 8 bit is getting redundant. so unicode is introduced which is 16 bit. to support all the characters


# Creating strings:

s='Hello'
s="Hello"
s=str("hello")
# handle multiline string 
s='''Hello'''
s="""Hello"""


# Concept of Indexing: in python string indexing start from 0 like other languages

c='Hello'
print(c[0]) # access first characters

# in python, there were 2 types of indexing

# 1. positive indexing -> starting first to last -> access first str[0]
# 2. negative indexing -> starting last to first -  but access last str[-1]
print(c[-1]) # 'o'



# Slicing:
str="Hello World"

print(str[0:5]) # Hello -> the last index is not included

print(str[2:]) # llo World-> skip first 2 chars
print(str[:2]) # He -> from start to last

print(str[0:10:2]) # HloWr -> last param is the step,
print(str[0:10:-1]) # empty string-> need to use with negative indexing then negative step will work

### For reversing a string in python in easy way is:
print(str[::-1]) #dlroW olleH


# Edit and Delete a strings:

# Strings are Immutable data type.

c="hello"
# c[0]="X" # give error, can't assign value to a string cuz its immutable.
c="world" # you can completely re-assign a string but can't re-assign or edit a string
# c[5]="X" # it also gives error, can't add more characters to a string.. if we add then it will create a new string

# del c[0] # give error, not possible



# Operations on string

# Addition
c= "Hello" +"world" # add 2 string -> concatenation
print(c)

# Multiplication
print("hello" *5)