colors = ['red', 'green', 'blue'] # colors to use

states = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T'] # states in Australia to color

neighbors = { # neighbors of each state
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'Q', 'SA'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'V', 'SA'],
    'V': ['NSW', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'T': []
}

def isSafe(state, color, assignment): # check if it is safe to color state with color
    for neighbor in neighbors[state]: # check if any neighbor has the same color
        if neighbor in assignment and assignment[neighbor] == color: # if so, return false
            return False
    return True # if no neighbor has the same color, return true

def graphColoring(assignment, states): # recursive function to color the graph
    if len(states) == 0: # if all states have been colored, return true
        return assignment
    state = states[0]
    for color in colors: # try to color the state with each color
        if isSafe(state, color, assignment):
            assignment[state] = color # color the state with the color
            result = graphColoring(assignment, states[1:]) # recurse
            if result is not None:
                return result # if the result is not None, return it
            del assignment[state] # if the result is None, delete the color and try the next color
    return None 

def printSolution(assignment): # print the solution
    for state in states:
        print(state, "=", assignment[state])

if __name__ == '__main__':
    assignment = graphColoring({}, states) 
    printSolution(assignment)
    