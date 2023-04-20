# Class to represent an NFA
class NFA:
    def __init__(self, start, final):
        self.start = start  # Start state
        self.final = final  # Final state
        self.states = []    # List of states
        self.transitions = {}   # Dictionary of transitions


def parse_regex(regex, graphic, num_states):
    nfas = [] # List of NFA objects
    alphabet = [] # List of alphabet letters
    index = 0   # Keeps track of index location searching through regex
    already_scanned = 0  # Keeps track of values inside of parentheses that were already scanned in a recursion
    or_already_scanned = False # Keeps track of recursion on "or" operator

    for letter in regex:    # Begin parsing    
        if letter == "(" and or_already_scanned == False:  # Find innermost parentheses
            if already_scanned == 0:
                count = 1   # Increase count by 1 signifying one "("
                for x in range(index + 1, len(regex)):
                    if regex[x] == ")":
                        count -= 1  # Decrease count by 1 signifying one ")"
                    elif regex[x] == "(":
                        count += 1
                    if count == 0:  # Found two matching parentheses
                        break

                inner = regex[index + 1:x]  # Get the new regex in the parentheses
                nfa, alphabet, num_states = parse_regex(inner, graphic, num_states) # Recurse on the new regex
                nfas.append(nfa)    # After recursion, add nfa to list
            already_scanned += 1 # Notes that one "(" has been found
        
        elif letter == ")":
            already_scanned -= 1 # Notes that one ")" has been found

        elif letter == "|" and already_scanned == 0 and or_already_scanned == False:
            nfa = nfas.pop()  # Get nfa from list             
            or_already_scanned = True  # Set or_flag
            nfa2, new_alphabet, num_states = parse_regex(regex[index + 1:], graphic, num_states) # Get the second half of "or" operation
            nfa.transitions.update(nfa2.transitions)    # Combine dictionaries
            for x in nfa2.states:   # Append states between two nfas
                nfa.states.append(x)
            for x in new_alphabet:  # Append alphabet between two nfas
                if x not in alphabet:
                    alphabet.append(x)

            new_start = "q" + str(num_states)   # Create two new states
            new_final = "q" + str(num_states + 1)
            nfa.states.append(new_start)
            nfa.states.append(new_final)
            num_states += 2

            nfa.transitions[(new_start, nfa.start)] = "E"   # Add transitions
            nfa.transitions[(new_start, nfa2.start)] = "E"
            nfa.transitions[(nfa.final, new_final)] = "E"
            nfa.transitions[(nfa2.final, new_final)] = "E"

            graphic.write(new_start + "->" + nfa.start + " [label=E];\n")   # Write to file
            graphic.write(new_start + "->" + nfa2.start + " [label=E];\n")
            graphic.write(nfa.final + "->" + new_final + " [label=E];\n")
            graphic.write(nfa2.final + "->" + new_final + " [label=E];\n")
         
            nfa.start = new_start   # Reset start and final states in nfa
            nfa.final = new_final
            nfas.append(nfa)

        elif letter == "*" and already_scanned == 0 and or_already_scanned == False:
            nfa = nfas.pop() # Get NFA from list
            new_start = "q" + str(num_states)   # Create two new states
            new_final = "q" + str(num_states + 1)
            nfa.states.append(new_start)
            nfa.states.append(new_final)
            num_states += 2

            nfa.transitions[(new_start, nfa.start)] = "E"   # Add transitions
            nfa.transitions[(new_start, new_final)] = "E"
            nfa.transitions[(nfa.final, nfa.start)] = "E"
            nfa.transitions[(nfa.final, new_final)] = "E"

            graphic.write(new_start + "->" + nfa.start + " [label=E];\n")   # Write to file
            graphic.write(new_start + "->" + new_final + " [label=E];\n")
            graphic.write(nfa.final + "->" + nfa.start + " [label=E];\n")
            graphic.write(nfa.final + "->" + new_final + " [label=E];\n")
         
            nfa.start = new_start   # Reset start and final states in nfa
            nfa.final = new_final
            nfas.append(nfa)

        elif letter == "+" and already_scanned == 0 and or_already_scanned == False:
            nfa = nfas.pop() # Get NFA from list
            nfa.transitions[(nfa.final, nfa.start)] = "E"   # Add transition
            graphic.write(nfa.final + "->" + nfa.start + " [label=E];\n")   # Write to file
            nfas.append(nfa)

        elif already_scanned == 0 and or_already_scanned == False:
            nfas.append(NFA(num_states, num_states))    # Create a new nfa
            nfa = nfas.pop()    # Get the newly added nfa
            if letter not in alphabet:  # Keep track of alphabet
                alphabet.append(letter)

            nfa.start = "q" + str(num_states)   # Create two new states
            nfa.final = "q" + str(num_states + 1)
            nfa.states.append(nfa.start)
            nfa.states.append(nfa.final)
            num_states += 2
            
            nfa.transitions[(nfa.start, nfa.final)] = letter    # Add transition
            graphic.write(nfa.start + "->" + nfa.final + " [label=" + letter + "];\n")  # Write to file
            nfas.append(nfa)
        index += 1  # Increment index
    nfa = nfas.pop(0) # Get the first NFA from the list

    while nfas: # Concatenate all nfas in list
        nfa2 = nfas.pop(0) # Get the next NFA from the list
        nfa.transitions[(nfa.final, nfa2.start)] = "E"  # Add transition
        graphic.write(nfa.final + "->" + nfa2.start + " [label=E];\n")  # Write to file
        nfa.transitions.update(nfa2.transitions)    # Combine dictionaries
        for x in nfa2.states:   # Append states between two nfas
            nfa.states.append(x)
        nfa.final = nfa2.final  # Reset final state
        
    return nfa, alphabet, num_states    # Return the final nfa and the alphabet and num_states for recursion