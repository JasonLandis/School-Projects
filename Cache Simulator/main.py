# Date: 3/14/2023
# Class: CS4541
# Assignment: Cache Simulator
# Author: Jason Landis
# Email: jason.e.landis@wmich.edu

def main():
    user_string = input(">> ")
    if user_string == "q":
        exit()

    # Get values from input
    try:           
        set_index_bits, associativity, block_bits, trace_file = user_string.split(" ")[:4]
        set_index_bits = int(set_index_bits)
        associativity = int(associativity)
        block_bits = int(block_bits)
        filename = "wmucachelab2/traces/" + trace_file + ".trace"
        try:
            cache_simulator(set_index_bits, associativity, block_bits, filename, "n")

        # If the file name is incorrect
        except FileNotFoundError:
            print("Incorrect file name\n"
                  "Enter the name of the file without the .trace extension or the parent directories\n")
            main()

    # If the input is incorrect
    except ValueError:
        print("Incorrect input")
        print("Usage: [Set index bits] [Associativity] [Block bits] [Trace file]\n")
        main()


def cache_simulator(set_index_bits, associativity, block_bits, trace_file, verbose):
    # Calculate the cache parameters
    num_sets = 2 ** set_index_bits
    num_blocks_per_set = associativity
    
    # Initialize the cache
    cache = [[] for x in range(num_sets)]
    
    # Initialize the performance counters and string used in verbose mode
    hit_count = 0
    miss_count = 0
    eviction_count = 0
    string = ""
    
    # Return the set index for the given address using bitwise shift
    def get_index(address):
        set_index = (address >> block_bits) % num_sets        
        return set_index
    
    # Determine if the block is in the cache
    def lookup(address): 
        nonlocal hit_count, miss_count, string
        set_index = get_index(address)
        tag = address >> (block_bits + set_index_bits)
        
        # See if the block is in the cache
        for x in range(num_blocks_per_set):
            if len(cache[set_index]) > x and cache[set_index][x][0] == tag:
                # Block found in the cache, increment hit counter and append to verbose string
                hit_count += 1
                string += "hit "
                return
        
        # Block not found in the cache, increment miss counter and append to verbose string
        miss_count += 1
        string += "miss "
        return
    
    # Evict the least recently used block in the set
    def evict_block(set_index):
        nonlocal eviction_count, string

        # Increment eviction counter and append to verbose string        
        eviction_count += 1
        string += "eviction "

        # Remove the least recently used block from the set
        block = cache[set_index].pop(0)
        return block
    
    # Insert a block into the cache
    def insert(address):
        set_index = get_index(address)
        tag = address >> (block_bits + set_index_bits)
        
        # Check if the block is already in the cache
        for x in range(num_blocks_per_set):
            if len(cache[set_index]) > x and cache[set_index][x][0] == tag:

                # Move it to the end of the list to mark it as most recently used
                block = cache[set_index].pop(x)
                cache[set_index].append(block)
                return
        
        # Block not in the cache, evict the least recently used block if the set is full
        if len(cache[set_index]) == num_blocks_per_set:
            evict_block(set_index)
        
        # Add the new block to the end of the set as the most recently used
        cache[set_index].append((tag, 1))
    
    # Process the trace file
    with open(trace_file, 'r') as f:
        for line in f:

            # Skip empty lines
            if line == " ":
                continue

            # skips "I" operations
            elif line[0] == " ":
                line = line[1:-1]         
                op = line[0]
                split_line = line[2:]
                address, size = split_line.split(",")
                address = int(address, 16)
                size = int(size)

                # Determines hits, misses, and evictions
                lookup(address)
                insert(address)
                if op == 'M':                    
                    insert(address)
                    lookup(address)

                # Print the verbose string if verbose mode is enabled
                if verbose == "y":
                    print(line, string)
                    string = ""                                
    
    # Print the performance counters
    print("hits:{} misses:{} evictions:{}\n".format(hit_count, miss_count, eviction_count))
    verbose = input("Run again in verbose mode? (y/n) ")

    # Run the cache simulator again in verbose mode
    if verbose == "y":
        cache_simulator(set_index_bits, associativity, block_bits, trace_file, verbose)
    print()
    main()

if __name__ == "__main__":
    main()
                 