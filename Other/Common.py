array = [1, 'b', 1, 'a', 2, 6, 'a', 3, 'b', 'b', 9, 3, 2]
dict = {}

count = 0
for x in array:
    for y in array:
        if x == y:
            count += 1
    dict[x] = count            
    count = 0

Max = max(dict, key = lambda x: dict[x])
print(Max)

