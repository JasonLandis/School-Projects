import csv
import timeit
import numpy as np

Time = []
Bubble = ["bubble sort"]
Insert = ["insertion sort"]
Quick = ["quick sort"]
Tim = ["tim sort"]


def main():
    my_sort(bubble, Bubble)
    my_sort(insertion, Insert)
    my_sort(quick, Quick)
    my_sort(tim, Tim)
    amounts = ["n", 10, 50, 100, 500, 1000, 5000]
    filename = "sorting_times.csv"
    with open(filename, 'w', newline='') as file:
        write = csv.writer(file)
        for w in range(7):
            write.writerow(
                [amounts[w], Bubble[w], Insert[w], Quick[w], Tim[w]])
        file.close()


def my_sort(function, List):
    n = [10, 50, 100, 500, 1000, 5000]
    num = 0
    count = 1
    while num <= 5:
        x = n[num]
        while count <= 10:
            array = np.random.randint(0, x, x)
            start = timeit.default_timer()
            try:
                function(array)
            except:
                function(array, 0, x - 1)
            Time.append(timeit.default_timer() - start)
            count += 1
        total = sum(Time)
        List.append(total / 10)
        Time.clear()
        count = 1
        num += 1


def bubble(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def insertion(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def quick(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        p = partition(array, low, high)
        quick(array, low, p - 1)
        quick(array, p + 1, high)


def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)


def tim(array):
    array.sort()


main()
