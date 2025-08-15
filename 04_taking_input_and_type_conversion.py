# Taking User Input

# input()
# first_num=input("Enter your first num: ") # it takes a argument called "prompt" where we can prompt to user
# second_num=input("Enter your second num:")

# result=first_num+second_num
# print(result)
# if we pass number, the input() takes it as a string only because for generic input

# if get integer from user we need to do type conversion
# what ever we are accepting from user input in python is in string type only.


# Type Conversion is 2 types - Implicit and Explicit

# 1. Implicit - python is smarter enough to convert it.
print(5+5.5) # it implicitly doing the type conversion then add it.
#10.5

# 2. Explicit
print(int("55")+50) # doing explicit type conversion - output 105

print(int("5.5")) #give error- in string decimal not supported -invalid literal for int() with base 10: '5.5'
print(float("5.5")) #it will not give any error


