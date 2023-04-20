# Date: 4/20/2023
# Class: CS4541
# Assignment: Memory Allocator
# Author: Jason Landis


class Block:
    def __init__(self, header, payload, footer):
        self.header = header    # Size of block in hex before payload
        self.payload = payload  # Allocated memory block
        self.footer = footer    # Size of block in hex after payload
        self.index = [] # Index of block in memory


def first(block):   # First fit
    for x in range(len(WORDS) - 1):
        if WORDS[x] >= block.header and WORDS[x + 1] == 0:  # Check if block can fit in memory
            index = x   # Get index of block
            return index, True  # Return index of block
    return 0, False # Return 0 if block cannot fit in memory


def best(block):    # Best fit
    block_locations = {}   
    for x in range(len(WORDS) - 1):
        if WORDS[x] >= block.header and WORDS[x + 1] == 0:  # Check if block can fit in memory
            block_locations[x] = WORDS[x]   # Add block to dictionary
    if len(block_locations) == 0:   # Check if block can fit in memory
        return 0, False # Return 0 if block cannot fit in memory
    temp = min(block_locations.values())
    for x in block_locations.keys():    # Find block with smallest size
        if block_locations[x] == temp:
            index = x   # Get index of block
            break
    return index, True  # Return index of block


def myalloc(size):  # Allocate memory block
    global WORDS    # Number of words in memory
    global INDEX   # Index of block in memory
    global FIRST   # First fit
    global BEST    # Best fit

    rem = size % 8  # Check if size is divisible by 8
    if rem != 0:
        size += 8 - rem    # Round up to nearest multiple of 8

    block = Block(size + 9, size / 4, size + 9)   # Create block
    
    if FIRST:   # First fit
        INDEX, can_fit = first(block)
    elif BEST:  # Best fit
        INDEX, can_fit = best(block)
    
    if not can_fit: # Check if block can fit in memory
        mysbrk(int(size/4)) # Extend memory

    WORDS[INDEX] = block.header    # Write header to memory
    INDEX += 1
    for x in range(int(block.payload)):    # Write payload to memory
        WORDS[INDEX] = 1
        block.index.append(INDEX)
        INDEX += 1
    WORDS[INDEX] = block.footer    # Write footer to memory
    INDEX += 1

    if WORDS[INDEX + 1] == 0:   # Check if next block is free
        WORDS[INDEX] = (len(WORDS) * 4) - (INDEX * 4 + 4)    # Write final header to memory
        WORDS[-1] = (len(WORDS) * 4) - (INDEX * 4 + 4)   # Write final footer to memory

    return block


def myrealloc(size, ptr):   # Reallocate memory block
    myfree(ptr) # Free memory block
    return myalloc(size)    # Allocate new memory block


def myfree(ptr):    # Free memory block
    block = BLOCKS[ptr] # Get block from dictionary   
    for x in block.index:
        WORDS[x] = 0
    del BLOCKS[ptr] # Delete block from dictionary


def mysbrk(size):   # Extend memory
    WORDS.extend([0] * size)    # Extend memory by size
    if len(WORDS) > 100000: # Check if memory limit is exceeded
        print("Memory limit exceeded")
        exit()


def main():
    global WORDS    # Number of words in memory
    global BLOCKS   # Dictionary of blocks
    global INDEX    # Index of block in memory
    global FIRST    # First fit
    global BEST     # Best fit

    while True: # Run until user quits
        WORDS = [0] * 1000
        BLOCKS = {}
        INDEX = 0
        FIRST = False
        BEST = False

        WORDS[0] = 4000 # Set initial header
        WORDS[-1] = 4000    # Set initial footer

        command = input(">> ")

        if command.lower() == "q" or command.lower() == "":
            break

        command = command.split()

        outfile = open("output.out", "w")   # Create output file

        try:        
            file = open(command[0], "r")    # Open input file
            lines = file.readlines()    # Read lines from file

            if command[1].lower() == "first":
                FIRST = True
            elif command[1].lower() == "best":
                BEST = True
            else:
                print("Usage: <filename> <first/best>\n")
                continue

            for x in lines: # Iterate through lines in file
                line = x.split(', ')
                
                if line[0] == "a":  # Allocate memory
                    block = myalloc(int(line[1]))
                    BLOCKS[int(line[2])] = block

                elif line[0] == "r":    # Reallocate memory
                    block = myrealloc(int(line[1]), int(line[2]))
                    BLOCKS[int(line[3])] = block

                elif line[0] == "f":    # Free memory
                    myfree(int(line[1]))

            index = 0
            for x in WORDS: # Write memory to output file
                if x == 0:
                    outfile.write(str(index) + ", \n")
                elif x == 1:
                    outfile.write(str(index) + ", x\n")
                else:
                    outfile.write(str(index) + ", " + str(hex(x)) + "\n")
                index += 1

            outfile.close() # Close output file
            file.close()    # Close input file

        except FileNotFoundError:
            print("File not found\n")
            continue

        except KeyError:
            print("Error in input file\n")
            continue

        except IndexError:
            print("Error in input file\n")
            continue


if __name__ == "__main__":
    print("Usage: <filename> <first/best>")
    main()
