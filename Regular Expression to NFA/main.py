import re
import graphviz
from parse_regex import parse_regex
from nfa_simulator import nfa_simulator

def main():

    ### Diable below and enable below that to get regex from user input ###
    # with open ("input.txt", "r") as file:    # Open input file
    #    regex = file.readline().replace(" ","")   # Get regex from file

    regex = input("Enter a regular expression: ").replace(" ","")
    if regex == "q":
        exit()
        
    try:
        re.compile(regex)   # Checks if regex is valid    
    except re.error:
        print("Invalid regular expression")
        main()

    graphic = open("nfa.dot", "w")  # Create graphic file and write to it
    graphic.write("digraph nfa {\nrankdir=LR;\nnode [shape=circle];\n")

    nfa, alphabet, num_states = parse_regex(regex, graphic, 0)  # Get the final nfa and alphabet

    graphic.write(nfa.start + " [shape=square];\n") # Write remaining information to graphic
    graphic.write(nfa.final + " [shape=doublecircle];\n")
    graphic.write("label=\"Regex: " + regex + "\";\n")
    graphic.write("fontsize=25;\nlabelloc=t;\n}")
    graphic.close()

    with open('nfa.dot') as f:  # Open the graphic and render it
        dot_graph = f.read()
    graph = graphviz.Source(dot_graph)
    graph.render('nfa.gv', format='png')

    while True:
        string = input("Enter a string: ")
        if string == "q":
            break

        # Simulate string on nfa
        accepted, path = nfa_simulator(nfa.transitions, nfa.states, nfa.start, nfa.final, string)

        graphic = open("nfa.dot", "w")  # Create graphic file and write to it
        graphic.write("digraph nfa {\nrankdir=LR;\nnode [shape=circle];\n")

        nfa, alphabet, num_states = parse_regex(regex, graphic, 0)  # Get the final nfa and alphabet

        graphic.write(nfa.start + " [shape=square];\n") # Write remaining information to graphic
        graphic.write(nfa.final + " [shape=doublecircle];\n")

        if accepted:    # Write path to graphic
            for state in path:
                graphic.write(state + " [color=green3];\n") # Make states green
            index = 1
            for state in path[:len(path) - 1]:
                graphic.write(state + "->" + path[index] + " [label=\"" + str(index) + "\",color=green3];\n")    # Make path green
                index += 1
            graphic.write("label=\"Regex: " + regex + "\nString: " + string + "\nAccepted\";\n")    # Write string and regex to graphic

        else:
            for state in path:
                graphic.write(state + " [color=red];\n")    # Make states red
            index = 1
            for state in path[:len(path) - 1]:
                graphic.write(state + "->" + path[index] + " [label=\"" + str(index) + "\",color=red];\n")   # Make path red
                index += 1
            graphic.write("label=\"Regex: " + regex + "\nString: " + string + "\nRejected\";\n")    # Write string and regex to graphic

        graphic.write("fontsize=25;\nlabelloc=t;\n}")
        graphic.close()

        with open('nfa.dot') as f:  # Open the graphic and render it
            dot_graph = f.read()
        graph = graphviz.Source(dot_graph)
        graph.render('nfa.gv', format='png')

    main()  # Recurse


if __name__ == '__main__':
    main()
