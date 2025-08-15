# Break - used for terminating the loop

for i in range(1,11):
    if i==5:
        break
    print(i)

# Continue- used for skip rest of code present in that block

for i in range(1,11):
    if i==5:
        continue    # it will not print i
    print(i)
    
    
# Pass - not very useful, when not sure which code to be written we can write pass 

for i in range(1,11):
    pass  # it just used to not get any error
