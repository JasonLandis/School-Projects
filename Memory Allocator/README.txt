Date: 4/20/2023
Class: CS4541
Assignment: Memory Allocator
Author: Jason Landis
Email: jason.e.landis@wmich.edu

OS: Windows 10
IDE: Visual Studio Code
Language: python

Once you run the main.py program you will see

Usage: <filename> <first/best>
>> 

Example use:
>> input.in first

At the prompt (>>) input the filename that the data will be read from followed by a space followed 
by first or best fit. My program will apply first or best fit on an implicit free list

You can use the input.in file to input any data you wish to test, and the resulting data will be 
placed in the output.out file

If the program has run correctly, you will see another prompt. At this point you can navigate to the
output.out file to see the results

In my output.out file, I display the locations in memory that are allocated

For example:

Input file
a, 5, 0
a, 10, 1
f, 0

Output file
0, 0x11         # This 0x11 header implies the beginning of an address of 8 bytes (created by a, 5, 0)
1,              # Since this area was freed (f, 0), there are no x's indicating open memory
2, 
3, 0x11         # This 0x11 header implies the end of an address of 8 bytes
4, 0x19         # This 0x19 header implies the beginning of an address of 16 bytes (created by a, 10, 0)    
5, x            # Since this area is not freed, there are x's implying it is being used
6, x
7, x
8, x
9, 0x19
10, 0xf74       # This is the remaining allocated memory in the heap
11, 
...
999, 0xf74

I remove the place holders and just began with the header of the first slot of memory allocated

You can try some other examples yourself to get a better understanding of how it works
If not, you can see the examples folder which contains an example of how my memory allocater
handles first and best fit

If there is an error in the input file, my program will notify you
If there the heap has exceeded 100000 words, the program will notify you and exit

References:
For references I stuck to using WMU material such as lecture slides and videos
