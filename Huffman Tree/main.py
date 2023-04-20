# The "node" class obtains the letter, the frequency of the letter, the value of the
# nodes to the left and right of thr original node, and initializes the huffman values
# which will either be 0 or 1
class node:
    def __init__(self, letter, freq, left=None, right=None):
        self.letter = letter
        self.freq = freq
        self.left = left
        self.right = right
        self.huff = ''


# Lists for letters and frequency
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

freq = [0.073, 0.009, 0.030, 0.044, 0.130, 0.028, 0.016, 0.035, 0.074, 0.002, 0.003, 0.035, 0.025, 0.078, 0.074, 0.027, 0.003, 0.077, 0.063, 0.093, 0.027, 0.013, 0.016, 0.005, 0.019, 0.001]

# creates an object for each letter, frequency pair in node and appends it to the list "nodes"
nodes = []
for n in range(len(letters)):
    nodes.append(node(letters[n], freq[n]))

# sorts nodes by frequency from smallest to highest, then obtains lowest two nodes, then
# sets the left node's huffman value to 0 and the right node's huffman value to 1
# I found this algorithm through a combination of stackoverflow and GeeksforGeeks and I
# understand how it works
while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.freq)
    left = nodes[0]
    right = nodes[1]
    left.huff = 0
    right.huff = 1

    # Creates a new node by adding lowest nodes' values, and removes used nodes from list.
    # the loop terminates once the nodes list only contains the parent node
    newNode = node(left.letter + right.letter,
                   left.freq + right.freq, left, right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)


info = []
# This function uses recursion to obtain the codes for each letter, once it detects
# a new node, it appends the letter, frequency, code, length of code, and frequency
# times length to list "info"


def getCodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        getCodes(node.left, newVal)
    if node.right:
        getCodes(node.right, newVal)
    if not node.left and not node.right:
        info.append([node.letter, node.freq, newVal,
                    len(newVal), (node.freq * len(newVal))])


# runs the above recursion algorithm on the parent node of the min heap, then sorts the
# list "info" by letter, then creates list of "freq x len" for later use
getCodes(nodes[0])
info = sorted(info, key=lambda x: x[0])
last_column = []
for n in info:
    last_column.append(n[4])

# outputs information and formats it nicely
print("Letter Frequency   Code   Length Freq X Len")
print("______ _________ ________ ______ __________")
print(' ')
for n in info:
    print(f"  {n[0]:1}      {n[1]:3}     {n[2]:8}    {n[3]:1}      {n[4]:3}")
print(' ')
print("The weigted minimum path length is:", sum(last_column))
