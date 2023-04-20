import timeit
import random

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Worst case array

rand_array = [] # Random array
for x in range(1, 11):    
    rand_array.append(random.randrange(1, 11))

rand_copy1 = rand_array[:] # Copies of original random array for later algorithms
rand_copy2 = rand_array[:]

Time = [] # Stores time

n = len(array) # Length of both arrays

# ----------------------------
# Standard selection algorithm
# ----------------------------

def partition(array, low, high):     
    pivotitem = array[low]
    i = low
    for j in range(low, high + 1):
        if array[j] < pivotitem:            
            array[i], array[j] = array[j], array[i]
            i += 1        
    array[i], pivotitem = pivotitem, array[i]    
    return i

def selection(array, low, high, k):
    index = partition(array, low, high)    
    if index - low == k - 1:        
        return array[index]
    if index - low > k - 1:        
        return selection(array, low, index - 1, k)    
    return selection(array, index + 1, high, k - index + low - 1)

# Timer for worst case over 100 cases
k = 10
for x in range(1000):
    start = timeit.default_timer()
    selection(array, 0, n - 1, k)
    Time.append((timeit.default_timer() - start) * 1000000000)

time = sum(Time) / 1000
Time.clear()

k = random.randrange(1, 11)

print("Worst case scenario")
print("Time complexity:", time, "nanoseconds")
print(" ")
print("Random array:", rand_array)
print("Searching for the k-th smallest element where k =", k)
print(" ")

# Timer for random case over 1000 cases
for x in range(1000):
    start = timeit.default_timer()
    result1 = selection(rand_array, 0, n - 1, k)
    Time.append((timeit.default_timer() - start) * 1000000000)

time = sum(Time) / 1000
Time.clear()

print("Selection algorithm on random array")
print("The k-th smallest element is", result1)
print("Time complexity:", time, "nanoseconds")
print(" ")

# -------------------------------------
# Median of medians selection algorithm
# -------------------------------------

def mmPartition(array, low, high):
    median = (high + low) // 2
    pivotitem = array[int(median)]
    i = low
    for j in range(low, high + 1):
        if array[j] < pivotitem:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], pivotitem = pivotitem, array[i]
    return i

def mmSelection(array, low, high, k):
    index = mmPartition(array, low, high)
    if index - low == k - 1:        
        return array[index]
    if index - low > k - 1:        
        return mmSelection(array, low, index - 1, k)    
    return mmSelection(array, index + 1, high, k - index + low - 1)

# Timer for median algorithm on random array over 1000 cases
for x in range(1000):
    start = timeit.default_timer()
    result2 = selection(rand_copy1, 0, n - 1, k)
    Time.append((timeit.default_timer() - start) * 1000000000)

time = sum(Time) / 1000
Time.clear()

print("Median of medians selection algorithm on random array")
print("The k-th smallest element is", result2)
print("Time complexity:", time, "nanoseconds")
print(" ")

# ------------------------------
# Randomized selection algorithm
# ------------------------------

def rPartition(array, low, high):
    rand = random.randrange(low, high + 1)     
    pivotitem = array[rand]    
    i = low
    for j in range(low, high + 1):
        if array[j] < pivotitem:            
            array[i], array[j] = array[j], array[i]
            i += 1              
    array[i], pivotitem = pivotitem, array[i]    
    return i

def rSelection(array, low, high, k):
    index = rPartition(array, low, high)
    if index - low == k - 1:
        return array[index]
    if index - low > k - 1:
        return rSelection(array, low, index - 1, k)
    return rSelection(array, index + 1, high, k - index + low - 1)

# Timer for randomized algorithm on random array over 1000 cases
for x in range(1000):
    start = timeit.default_timer()
    result3 = selection(rand_copy2, 0, n - 1, k)
    Time.append((timeit.default_timer() - start) * 1000000000)

time = sum(Time) / 1000
Time.clear()

print("Randomized selection algorithm on random array")
print("The k-th smallest element is", result3)
print("Time complexity:", time, "nanoseconds")
