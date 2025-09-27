
# Fibonacci series in python
def fibonacci_series(num):
    fib=[0,1]

    for i in range(num):
        fib.append(fib[i]+fib[i+1])
    return fib

print(fibonacci_series(10))