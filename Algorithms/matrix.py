import timeit

# Test matrices used in algorithm examples
one = [
[1]
]

emptyone = [[0]]

two = [
[1, 2], 
[1, 2]
]

emptytwo = [[0, 0], [0, 0]]

three = [
[1, 2, 3], 
[1, 2, 3], 
[1, 2, 3]
]

emptythree = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

four = [
[1, 2, 3, 4], 
[1, 2, 3, 4],
[1, 2, 3, 4],
[1, 2, 3, 4]
]

emptyfour = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

five = [
[1, 2, 3, 4, 5], 
[1, 2, 3, 4, 5],
[1, 2, 3, 4, 5],
[1, 2, 3, 4, 5],
[1, 2, 3, 4, 5]
]

emptyfive = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

record = []

# Matrix transpose algorithm
def transpose(old, new, n): 
    for x in range(n):
        for y in range(n):
            new[x][y] = old[y][x]

# Matrix multiplication algorithm
def multiply(old, new, n): 
    for x in range(n):
        for y in range(n):         
            new[x][y] = 0
            for z in range(n): 
                new[x][y] += old[x][z] * old[z][y]

# Algorithm to record average time taken to either transpose or multiply a matrix over 100 runs
def time(first, second, n, op):
    for x in range(100):
        start = timeit.default_timer()
        op(first, second, n)
        time = timeit.default_timer() - start
        time *= 1000000000
        record.append(time)
    total = sum(record)
    record.clear()
    total /= 100
    print(f"n = {n}: {total} nanoseconds")

# Formats output nicely
print(f"Average time durations\n")

print(f"Matrix Transpose")
time(one, emptyone, 1, transpose)
time(two, emptytwo, 2, transpose)
time(three, emptythree, 3, transpose)
time(four, emptyfour, 4, transpose)
time(five, emptyfive, 5, transpose)

print("\nMatrix Multiplication")
time(one, emptyone, 1, multiply)
time(two, emptytwo, 2, multiply)
time(three, emptythree, 3, multiply)
time(four, emptyfour, 4, multiply)
time(five, emptyfive, 5, multiply)