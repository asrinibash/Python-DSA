# Operators: Operators are used to perform operation on variables and values.

# 1. Arithmetic Operator
# 2. Comparison Operator
# 3. Logical Operator
# 4. Bitwise Operator
# 5. Assignment Operator
# 6. identity Operator
# 7. Membership Operator

# Arithmetic Operator:
x=5
y=2
print(x+y) # 7
print(x-y) # 3
print(x*y) # 10
print(x/y) # 2.5
print(x%y) # modulus operator for getting reminder # 1
print(x**y) #power-of operator 5 power 2 so 25
print(x//2) # integer division 2 limiting the decimal values


# Comparison Operator(Relational Operator) --getting output in booleans
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)


# Logical Operator - or, and, not
x=True
y=False

print(x or y) # if any one true it will true, in this case its true
print(x and y) # both values needs to be true, in this case its false
print(not x) # gives opposite value of value, in this case it will give false


# Bitwise Operator - Mainly working on Binary value
# Real project example of using these operators: Image processing and when creating image filters these are the combination of binary operators
x=2
y=3

print(x & y) # Bitwise and -> converting it to binary then performing operations. output is 2
print(x | y) # Bitwise or -> output is 3
print(x>>y) # right shift -> 0
print(x<<y) #left shift -> 24
print(~x) # one's complement -> -3


# Assignment Operator
a=3  # Here '=' is the assignment operator
# there were some variation of assignment operator

a+=3 # it means a= a+3 -> 6
a-=3 # a=a-3 -> 0
a*=3 # a=a*3 -> 9
a/=3 # a=a/3 -> 1


# **** IMPORTANT NOTES:\
    # there is not concept and syntax of increment or decrement operators like we used in c or java a++ and --b
# a++ -> give syntax error


# Identical Operator: is

a=2
b=2

# is -> is operator will check if they were same location or not 
print( a is b) # -> true

a="Hello"
b="Hello"
print(a is b) # True

a=[1,2,3]
b=[1,2,3]
print(a is b) # False -> By looking at similar its doesn't means they are in same location

a="Hello-world"
b='Hello-world'

print(a is b) # True --it will only just tell is they are in same memory location.


# Membership Operator: in , not in  or is , is not

a="Odisha"
print( "O" in a) # true
print("O" not in a) # false

a=[1,2,3]
print(5 in a) # false

a=(1,2,3)
print(2 in a) # True

a={1,1,2,3} 
print( 1 is not a) # True 

# Membership operator can be used in string,list, tuple,set


