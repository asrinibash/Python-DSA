import random

jackpot_num=random.randint(1,100)

u_input=int(input("Enter the number: "))
attempt=1

while u_input!=jackpot_num:
    if u_input<jackpot_num:
        print("Try Higher")
    elif u_input>jackpot_num:
        print("Try Lower")
    u_input=int(input("Enter the number again: "))
    attempt += 1
        
print("correct guess, you took",attempt, "attempt for guess the number.")