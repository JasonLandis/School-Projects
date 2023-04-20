# Simulates a string input on a NFA
def nfa_simulator(transitions, states, start, final, string, visited = None):
    if visited == None: # Keeps track of visited states
        visited = []
    current_state = start   # Set current state to start state
    new_current = current_state # Set new current state to current state
    path = [current_state] # Keeps track of path taken
    occurences = {} # Keeps track of transitions with the same letter
    num_occurences = 0  # Keeps track of number of transitions with the same letter
    end_flag = False    # Flag to check if end of string has been reached
    index = 0   # Keeps track of index of string
    
    while True:
        current_state = new_current # Set current state to new current state

        if index == len(string):    # Check if end of string has been reached
            string += "E"
            end_flag = True

        if current_state == final and string[index] == "E": # Check if string is accepted
            return True, path
        
        letter = string[index] # Get letter at index

        for state in states:    # Get all transitions from current state
            if (current_state, state) in transitions:   
                if transitions[(current_state, state)] == letter or transitions[(current_state, state)] == "E":
                    occurences[(current_state, state)] = transitions[(current_state, state)]
                    num_occurences += 1
        
        if num_occurences == 0: # Check if there are no transitions from current state
            return False, path

        for (current_state, state) in occurences:   # Check if there are multiple transitions with the same letter
            if occurences[(current_state, state)] == letter: 
                new_current = state
                index += 1
                if end_flag == True:    # Check if end of string has been reached
                    if new_current not in visited:  # Add new current state to visited if it has not been visited
                        visited.append(new_current)
                    else:
                        if num_occurences > 1:
                            index -= 1
                            continue
                        else:
                            return False, path
                else:
                    visited = []
                if num_occurences > 1:  # Check if there are multiple transitions with the same letter
                    num_occurences -= 1
                    accepted, new_path = nfa_simulator(transitions, states, new_current, final, string[index:], visited) # Recurse
                    if accepted == True:    # Check if string is accepted
                        for state in new_path:  # Add new path to path
                            path.append(state)
                        return True, path
                    else:
                        new_current = current_state # Set new current state to current state
                        index -= 1
               
            elif occurences[(current_state, state)] == "E": # Check if there is an epsilon transition
                new_current = state
                if new_current not in visited:  # Add new current state to visited if it has not been visited
                    visited.append(new_current)
                else:
                    if num_occurences > 1:
                        continue
                    else:
                        return False, path
                if num_occurences > 1:  # Check if there are multiple transitions with the same letter
                    num_occurences -= 1
                    accepted, new_path = nfa_simulator(transitions, states, new_current, final, string[index:], visited)    # Recurse
                    if accepted == True:    # Check if string is accepted
                        for state in new_path:  # Add new path to path
                            path.append(state)
                        return True, path
                    else:
                        if letter == "E":
                            index -= 1
                        new_current = current_state # Set new current state to current state

        num_occurences = 0  # Reset number of transitions with the same letter
        occurences = {} # Reset transitions with the same letter
        path.append(new_current)    # Add new current state to path
