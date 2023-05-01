# User Guide

## Before you use

To run the program in windows, you must have the following installed:

__Python (preferably the latest version)__  
__Regex__  
__Graphviz__  
__An IDE (optional)__  

The regex library should be installed with python.

### Installing Graphviz

To install the graphviz library, you will need to enter pip install graphviz in your terminal.
After this go to https://graphviz.org/download/ and install the latest version of Graphviz for windows. Once it has finished installing, unzip it and place the bin folder in your system's PATH. 

Now restart your IDE and run the program.

## During runtime

The program will prompt you to enter a regular expression

My program includes computation of only the following operators

__*  -  zero or more__  
__+  -  one or more__  
__|  -  or operator__  
__()  -  parentheses__  

Any other character entered will be processed as a terminal symbol

If you entered an invalid regular expression you will be notified and returned to the prompt.

After you enter the regular expression, go to the file nfa.gv.png, it will show you the new NFA.

Now you can enter a string to be processed. You can keep nfa.gv.png open because after you enter a string, it will show the path taken to generate that string in nfa.gv.png.
You will then be asked to enter another string.

If at any point you want to stop testing a string, press “q”. This will allow you to test another regular expression. If you want to exit the program, press “q” again.

You can also choose to enter the regular expression in the input.txt file
