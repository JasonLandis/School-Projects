Date: 3/14/2023
Class: CS4541
Assignment: Cache Simulator
Author: Jason Landis
Email: jason.e.landis@wmich.edu

OS: Windows 10
IDE: Visual Studio Code
Language: python

How to use the program:
Run the python program and you will see a prompt >>

Usage:
>> [set index bits] [associativity] [block bits] [trace file]
The trace file must only be the name without the .trace or the parent directories

Example:
>> 4 2 4 dave

Once the program will run once, it will ask if you want to run again in verbose mode
Hitting "y" will run the program again in verbose mode
Hitting anything else will return back to the >> prompt and you can try another input

Notes:
Any extra trace files used to test must be placed into the traces folder or an error will occur
Hitting "q" at the >> prompt will exit the program

Style:
I used snake case styling throughout my program
The multi-word variables and functions are lowercase and are split by an underscore

References:

https://stackoverflow.com/questions/141525/what-are-bitwise-shift-bit-shift-operators-and-how-do-they-work

This site helped me understand bitwise operators. I found it beneficial to 
use the right bitwise operation in some parts of my program

https://www.youtube.com/watch?v=pO_ntrdyqoM

This video went into detail on how to indicate hits and misses in cache memory
It helped me make the cache_simulator function in my program
