# Insertion sort algorithm
def insertion(array, *, key):
    for x in range(1, len(array)):
        pivot = array[x]
        for y in range(x - 1, -1, -1):
            if key(array[y]) <= key(pivot):
                break
            array[y + 1] = array[y]
        else:
            y -= 1
        array[y + 1] = pivot


# Quick sort algorithm
def quick(array, low, high, name):
    if high - low == 1:
        return array
    elif low < high:
        p = partition(array, low, high, name)
        quick(array, low, p - 1, name)
        quick(array, p + 1, high, name)


# Partition algorithm used in quick sort
def partition(array, low, high, name):
    x = (low - 1)
    pivot = array[high].get("Name")
    for y in range(low, high):
        if array[y].get("Name") <= pivot:
            x += 1
            array[x], array[y] = array[y], array[x]
    array[x + 1], array[high] = array[high], array[x + 1]
    return (x + 1)


# Binary search algorithm
def binary_search(array, low, high, name):
    if array[high].get("Name") >= array[low].get("Name"):
        mid = (high + low) // 2
        if array[mid].get("Name") == name:
            return mid
        elif array[mid].get("Name") > name:
            return binary_search(array, low, mid - 1, name)
        else:
            return binary_search(array, mid + 1, high, name)
