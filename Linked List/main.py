import csv
from doubleLinkedList import gamesLinkedList
from algorithms import *
import timeit

#
# PLAGIARISM DECLARATION
#
# 1. I know that plagiarism means taking and using the ideas, writings, programs,
# code, works, or inventions of another as if they were one’s own. I know that
# plagiarism not only includes verbatim copying, but also the extensive use of
# another person’s ideas without proper acknowledgement (which includes the
# proper use of quotation marks). I know that plagiarism covers the use of
# material found in textual sources and from the Internet.
#
# 2. I acknowledge and understand that plagiarism is wrong.
#
# 3. This assignment is my own work, or my group’s own unique group
# assignment. I acknowledge that copying someone else’s assignment, or part
# of it, is wrong, and that submitting identical work to others constitutes a
# form of plagiarism.
#
# 4. I have not allowed, nor will I in the future allow, anyone to copy my work
# with the intention of passing it off as their own work.
#

# Creates Link object from gamesLinkedList and stores each line in the
# csv file as a dictionary in a linked list. Also creates two list objects
# to use for sorting.
Link = gamesLinkedList()
ListInsert = []
ListQuick = []
filename = "games.csv"
with open(filename, 'r') as games:
    for line in csv.DictReader(games):
        Link.insert_end(line)
        ListInsert.append(line)
        ListQuick.append(line)


# simple list for maintaining timing data
Time = []

print("Number of elements in LinkedList:", Link.size(), "\n")
print("*** Linear Search Test ***\n")
print("Before sorting:\n")
Link.first_five()

# starts the linear search and repeats it 3 times total. Also creates a
# Names list to remember the randomly selected names for the binary search later
num = 1
Names = []
for x in range(3):
    name = Link.random()["Name"]
    print(' ')
    print("Search number " + str(num) + ":")
    print("Searching for '" + name + "'...")
    Names.append(name)

    # records the time for each find() function and stores it in the Time list
    for x in range(5):
        Start = timeit.default_timer()
        data = Link.linear_search(name)
        Time.append(timeit.default_timer() - Start)

    print("Single search time:", Time[0], "seconds.")
    print("Average search time:", sum(Time) / 5, "seconds.")

    # clears the time list to loop through again
    Time.clear()
    num += 1


# Runs the insertion sort algorithm on the List from the csv file, records the time,
# then stores it in a linked list
insertsortLink = gamesLinkedList()
Start = timeit.default_timer()
insertion(ListInsert, key=lambda x: x["Name"])
Time.append(timeit.default_timer() - Start)
for line in ListInsert:
    insertsortLink.insert_end(line)


# Runs the quick sort algorithm on the List from the csv file, records the time,
# then stores it in a linked list. Also creates a new Time list.
TimeQuick = []
quicksortLink = gamesLinkedList()
Start = timeit.default_timer()
quick(ListQuick, 0, len(ListQuick) - 1, name)
TimeQuick.append(timeit.default_timer() - Start)
for line in ListQuick:
    quicksortLink.insert_end(line)


# Displays sorted list from insertion sort algorithm
print(' ')
print("After sorting:\n")
insertsortLink.first_five()


# Displays elapsed time for insertion and quick sort algorithms
print(' ')
print("Time for insertion sort:", Time[0], "seconds.")
print("Time for quick sort:", TimeQuick[0], "seconds.\n")

print("*** Binary Search Test ***")


# Repeats steps shown above but uses binary search instead
num = 1
for name in Names:
    print(' ')
    print("Search number " + str(num) + ":")
    print("Searching for '" + name + "'...")

    for i in range(5):
        Start = timeit.default_timer()
        data = binary_search(ListQuick, 0, len(ListQuick) - 1, name)
        Time.append(timeit.default_timer() - Start)

    print("Single search time:", Time[0], "seconds.")
    print("Average search time:", sum(Time) / 5, "seconds.")

    Time.clear()
    num += 1


# Creates multiple lists needed for functions below. Timebin adds time for quick sort above.
# Titles, LinearSearch, and BinarySearch created as titles to be written to csv file.
Names = []
Timelin = []
Timebin = [TimeQuick[0]]
Titles = ["Searches"]
LinearSearch = ["Linear Search Time"]
BinarySearch = ["Binary Search Time"]


# Goes through 10 iterations of linear search through random names. Sums the time elapsed for each iteration as
# well as the previous iterations and appends it to the LinearSearch list.
for x in range(10):
    Start = timeit.default_timer()
    name = Link.random()["Name"]
    Link.linear_search(name)
    Timelin.append(timeit.default_timer() - Start)
    total = sum(Timelin)
    LinearSearch.append(total)
    Names.append(name)
    Titles.append(x)


# Goes through each name randomly selected in previous function. Does binary search on each name
# and appends time to BinarySearch
for name in Names:
    Start = timeit.default_timer()
    binary_search(ListQuick, 0, len(ListQuick) - 1, name)
    Timebin.append(timeit.default_timer() - Start)
    total = sum(Timebin)
    BinarySearch.append(total)


# Creates a csv file and writes the information from above into table that can easily be
# formatted into excel
filename = "searchTimes.csv"
with open(filename, 'w', newline='') as file:
    write = csv.writer(file)
    for x in range(11):
        write.writerow([Titles[x], LinearSearch[x], BinarySearch[x]])
    file.close()

print(' ')
print("Break point m = 4 between repeated linear searches and sort-once & multiple binary searches.")
