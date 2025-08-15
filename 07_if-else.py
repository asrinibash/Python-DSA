# if- else is called conditional statement

a=10
b=15

if a==0:
    print("Yes")   # We have to give some space the next line of 'if', likewise we given for this line before print
    
elif b=="10":      # not else if -> its elif
    print("Yes")
else:
    print("No")    # same type syntax also for else
    
    
email=input("Enter email : ")

#Example of if-else, elif, if-else ladder and nested if-else

if '@' in email:
    password=input("Enter Password :")
    if email == "srinu@gmail.com" and password=="1234":
        print("Login Success, Welcome!")
    elif email=="srinu@gmail.com" and password!="1234":
        print("Password incorrect!")
        password=input(" Re-Enter Password")
        if password=="1234":
            print("Login Success, Welcome!")
        else:
            print("Still incorrect")
    else:
        print("Invalid Credentials")
else:
    print("Email is not valid")