# Algorithm: Hopcroft's DFA Minimization Algorithm
def hopcroft_minimization(states, alphabet, transitions, start_state, accepting_states):
    accepting_states = set(accepting_states)
    non_accepting_states = set(states) - accepting_states
    partitions = [accepting_states, non_accepting_states]
    for symbol in alphabet:
        for i, partition in enumerate(partitions):
            new_partitions = {}
            for state in partition:
                next_state = transitions.get((state, symbol))
                if next_state:
                    for j, p in enumerate(partitions):
                        if next_state in p:
                            if j not in new_partitions:
                                new_partitions[j] = set()
                            new_partitions[j].add(state)
                            break
            if len(new_partitions) > 1:
                partitions.pop(i)
                for new_partition in new_partitions.values():
                    partitions.append(new_partition)
    state_map = {}
    minimized_trans = {}
    new_states = set()
    for i, partition in enumerate(partitions):
        partition_name = ','.join(sorted(partition))
        state_map[partition_name] = i
        new_states.add(partition_name)
        for symbol in alphabet:
            next_state = transitions.get((next(iter(partition)), symbol))
            if next_state:
                for j, p in enumerate(partitions):
                    if next_state in p:
                        new_partition_name = ','.join(sorted(p))
                        minimized_trans[(partition_name, symbol)] = new_partition_name
                        break
    for i, partition in enumerate(partitions):
        if start_state in partition:
            minimized_start_state = ','.join(sorted(partition))
            break
    minimized_accepting_states = set(','.join(sorted(partition)) for partition in partitions if partition & accepting_states)

    # write to file
    with open('output.txt', 'w') as f:
        f.write(','.join(new_states) + '\n')
        f.write(','.join(alphabet) + '\n')
        f.write(minimized_start_state + '\n')
        f.write(','.join(minimized_accepting_states) + '\n')
        for (state, symbol), next_state in minimized_trans.items():
            f.write(','.join([state, symbol, next_state]) + '\n')
        
    return new_states, alphabet, minimized_trans, minimized_start_state, minimized_accepting_states


# Simulates a string input on a DFA
def dfa_simulator(transitions, start_state, accepting_states, input_string):
    current_state = start_state
    path = [current_state]
    for symbol in input_string:
        if (current_state, symbol) not in transitions:
            return False, path
        current_state = transitions[(current_state, symbol)]
        path.append(current_state)
        
    return current_state in accepting_states, path


# Reads a DFA from a file
def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    states = set(lines[0].strip().split(','))
    alphabet = lines[1].strip().split(',')
    start_state = lines[2].strip()
    accepting_states = set(lines[3].strip().split(','))
    transitions = {}
    for line in lines[4:]:
        parts = line.strip().split(',')
        transitions[(parts[0], parts[1])] = parts[2]

    return states, alphabet, transitions, start_state, accepting_states


# Shows both the original DFA and the minimized DFA and allows the user to input strings to test
def main():
    while True:
        filename = input('Enter filename: ')
        if filename == 'q':
            break
        filename += '.txt'
        states, alphabet, transition, start_state, accept_states = read_file(filename)
        min_states, min_alphabet, min_transition, min_start_state, min_accept_states = hopcroft_minimization(states, alphabet, transition, start_state, accept_states)
        print("Minimized DFA: ")
        print("States: ", min_states)
        print("Alphabet: ", min_alphabet)
        print("Transitions: ")
        for (state, symbol), next_state in min_transition.items():
            print(state, symbol, next_state)
        print("Start State: ", min_start_state)
        print("Accepting States: ", min_accept_states)
        print()
        while True:
            input_string = input('Enter string: ')
            if input_string == 'q':
                break
            accepted, path = dfa_simulator(transition, start_state, accept_states, input_string)
            if accepted:
                print('DFA: Accepted')
                print('Path:', ' -> '.join(path) + '\n')
            else:
                print('DFA: Rejected')
                print('Path:', ' -> '.join(path) + '\n')        
            accepted, path = dfa_simulator(min_transition, min_start_state, min_accept_states, input_string)
            if accepted:
                print('Minimized DFA: Accepted')
                print('Path:', ' -> '.join(path) + '\n')
            else:
                print('Minimized DFA: Rejected')
                print('Path:', ' -> '.join(path) + '\n')


if __name__ == '__main__':
    main()