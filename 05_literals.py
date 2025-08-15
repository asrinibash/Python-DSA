# Literals in python is the raw data given in a variable.

# There were 4 types of literals
#   1. Numeric Literal
#   2. String Literal
#   3. Boolean Literal
#   4. Special Literal

# 1. **Numeric Literal:
# there are 3 type of numeric data types : numeric,float,complex

# numeric
import string


a=0b1010 # binary: for binary we need to use "0b" in first.. it will taken as binary value
b=100 # decimal
c=0o310 # Octal Literal
d=0x12c # hexadecimal literal

b=100
print(a)# it will print in decimal
print(b)# Output - 100
print(c)# 200
print(d)# 300
# All are print in the decimal

# float
float_1=10.5
float_2=1.5e2 # for bigger number we are using this
float_3=1.5e-3 # for very smaller number we are using 10 to the power in minus
print(float_1,float_2,float_3)
#Output: 10.5 150.0 0.0015

# complex
# x=0+3.14j
# print(x) # output- 3.14j


# 3. **String Literals
string='This is line'
strings="This is line" # there is no difference between single and double inverted commas
char="c" # there is char datatype is python, everything it treated as string only. this also taken as string only but we can initialise a sing character.
multiline_str="""this is multiline str""" #when ever we taken a big string input from user we we use this. mainly use in big strings
unicode=u"\U0001f600\U0001f606\U0001f923" # we can receive unicode string in python also like emojis 😊
raw_str=r"raw \ string" #useful when printing like html, we ca use inside \n here.

print(string) # This is line
print(strings) # This is line
print(char) #c
print(multiline_str) # this is multiline str
print(unicode) # output: 😀😆🤣
print(raw_str) # raw \ string


# 3.** Boolean type conversion

bool_a=True+10 # doing implicit type conversion, taking true is value 1
bool_b=False+10 # same here also, taking false as 0

print(bool_a) #output- 11
print(bool_b) #output- 10


# 4.** Special Literal

sp=None # None means absence of anything. we will use it in most.
print(sp) #output- None

# there is no declaration of variable concept in python, if required then we can implement by assigning None value to it.
# k # it will give error, we cant declare a variable, if we declare then have to use it.

k=None #for declaration we need to use it like this.





