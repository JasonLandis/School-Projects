def fib(x, y):       
    z = x + y
    if z > 100:
        exit()
    print(z)
    fib(y, z)


fib(1, 1)
