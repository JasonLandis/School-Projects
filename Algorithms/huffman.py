import random
import timeit

english = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

english_freq = [0.073, 0.009, 0.030, 0.044, 0.130, 0.028, 0.016, 0.035, 0.074, 0.002, 0.003, 0.035, 0.025, 0.078, 0.074, 0.027, 0.003, 0.077, 0.063, 0.093, 0.027, 0.013, 0.016, 0.005, 0.019, 0.001]

cyrillic = ['О', 'Е', 'А', 'И', 'Н', 'Т', 'С', 'Л', 'В', 'Р', 'К', 'М', 'Д', 'П', 'Ы', 'У', 'Б', 'Я', 'Ь', 'Г', 'З', 'Ч', 'Й', 'Ж', 'Х', 'Ш', 'Ю', 'Ц', 'Э', 'Щ', 'Ф', 'Ё', 'Ъ']

cyrillic_freq = [0.1118, 0.0875, 0.0764, 0.0709, 0.0678, 0.0609, 0.0497, 0.0496, 0.0438, 0.0423, 0.0330, 0.0317, 0.0309, 0.0247, 0.0236, 0.0222, 0.0201, 0.0196, 0.0184, 0.0172, 0.0148, 0.0140, 0.0121, 0.0101, 0.0095, 0.0072, 0.0047, 0.0039, 0.0036, 0.0030, 0.0021, 0.0020, 0.0002]

hiragana = ['い', 'し', 'う', 'ん', 'の', 'か', 'た', 'と', 'す', 'で', 'に', 'く', 'は', 'て', 'こ', 'ま', 'な', 'が', 'き', 'る', 'り', 'を', 'も', 'れ', 'つ', 'じ', 'ら', 'あ', 'せ', 'ち', 'お', 'さ', 'わ', 'だ', 'そ', 'け', 'よ', 'ど', 'え', 'み', 'ひ', 'め', 'ろ', 'ば', 'ぶ', 'や', 'ほ', 'ね', 'ふ', 'げ', 'ご', 'ぎ', 'む', 'び', 'ず', 'べ', 'ざ', 'ぼ', 'ぜ', 'ぐ', 'ゆ', 'ぷ', 'へ', 'ぞ', 'ぱ', 'づ', 'ぽ', 'ぴ', 'ぺ', 'ぬ', 'ぢ']

hiragana_freq = [0.0634, 0.0497, 0.0493, 0.0492, 0.0398, 0.0365, 0.0362, 0.0330, 0.0310, 0.0289, 0.0262, 0.0261, 0.0260, 0.0253, 0.0251, 0.0246, 0.0240, 0.0221, 0.0220, 0.0212, 0.0181, 0.0174, 0.0169, 0.0162, 0.0160, 0.0158, 0.0152, 0.0141, 0.0132, 0.0121, 0.0120, 0.0112, 0.0111, 0.0103, 0.0101, 0.0093, 0.0092, 0.0085, 0.0084, 0.0076, 0.0066, 0.0063, 0.0051, 0.0050, 0.0046, 0.0045, 0.0044, 0.0042, 0.0041, 0.0034, 0.0033, 0.0030, 0.0029, 0.0028, 0.0026, 0.0024, 0.0021, 0.0020, 0.0019, 0.0018, 0.0017, 0.0016, 0.0015, 0.0014, 0.0012, 0.0007, 0.0006, 0.0005, 0.0003, 0.0002, 0.0000]

arabic = ['ء', 'ؤ', 'ئ', 'ا', 'آ', 'أ', 'إ', 'ب', 'ة', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ى', 'ي']

arabic_freq = [0.0031, 0.0009, 0.0028, 0.1250, 0.0015, 0.0289, 0.0100, 0.0467, 0.0142, 0.0261, 0.0087, 0.0123, 0.0186, 0.0079, 0.0267, 0.0096, 0.0420, 0.0052, 0.0247, 0.0073, 0.0104, 0.0044, 0.0050, 0.0018, 0.0401, 0.0033, 0.0284, 0.0269, 0.0204, 0.1207, 0.0652, 0.0661, 0.0508, 0.0580, 0.0129, 0.0636]


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


heap_time = [0] # Stores time for min-heap construction
huffman_time = [] # stores time for Huffman tree generation


def main(List, freq):
    # creates an object for each letter, frequency pair in node and appends it to the list "nodes"
    nodes = []    
    for n in range(len(List)):
        nodes.append(node(List[n], freq[n]))

    # Starts timer for Huffman tree Generation
    huffman = timeit.default_timer()        
    while len(nodes) > 1:
        # Constructs the min-heap and records the time to do so
        heap = timeit.default_timer()        
        nodes = sorted(nodes, key=lambda x: x.freq)
        heap_time.append((timeit.default_timer() - heap))        

        # Assigns Huffman values
        left = nodes[0]
        right = nodes[1]
        left.huff = 0
        right.huff = 1

        # Generates Huffman tree        
        newNode = node(left.letter + right.letter, left.freq + right.freq, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
           
    # Stores Huffman time
    huffman_time.append((timeit.default_timer() - huffman))

    # runs getCodes function and sorts list info by letter
    getCodes(nodes[0])
    info_sort = sorted(info, key=lambda x: x[0])
    
    # last_column list is used for retrieving the total weighted external path of the tree
    last_column = []
    for n in info_sort:
        last_column.append(n[4])

    # Ensures that the program only prints the English, Cyrillic, Hiragana, and Arabic lists
    # and prints timing data for the randomized freqeuncy lists
    if sum(count) < 4:
        printMain(info_sort, last_column)
    else:
        printRand()

    # Resets all lists and adds 1 to count
    count.append(1)
    nodes.clear()
    info.clear()
    huffman_time.clear()
    heap_time.clear()
    heap_time.append(0)


# Retrieves all Huffman codes and stores letter, frequency, code, length of code,
# and weighted length in info list 
info = []
def getCodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        getCodes(node.left, newVal)
    if node.right:
        getCodes(node.right, newVal)
    if not node.left and not node.right:
        num = str(node.freq * len(newVal))        
        info.append([node.letter, node.freq, newVal,
                    len(newVal), float(num[:6])])


# These lists are used for printing output
display_titles = ['English', 'Cyrillic', 'Hiragana', 'Arabic', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
count = []


# Prints English, Cyrillic, Hiragana, and Arabic data
def printMain(info_sort, last_column):
    print(display_titles[sum(count)])
    print("--------------------------------------------------------")    
    print("Letter  Frequency      Code      Length  Weighted Length")
    print("______  _________  ____________  ______  _______________\n")    
    for n in info_sort:
        print(f"  {n[0]:1}      {n[1]:6}    {n[2]:13}  {n[3]:2}      {n[4]:3}")
    print()    
    print("The weigted minimum path length for " + display_titles[sum(count)] + " is:", sum(last_column))
    print()
    return


# Creates a character and frequency list where the frequencies are random values
# between 1 and 100. Runs them in the main function
char = []
freq = []
def randomFreq(n):
    count = 1    
    for x in range(n):
        char.append(count)
        freq.append(random.randrange(1, 101))
        count += 1
    main(char, freq)
    char.clear()
    freq.clear()


# Prints timing data for randomized frequency lists
def printRand():
    print("n =", display_titles[sum(count)])
    print("Time for min-heap construction:", sum(heap_time) * 1000000, "microseconds")
    print("Time for Huffman tree generation:", huffman_time[0] * 1000000, "microseconds\n")    
    return


# Function calls and output formatting
main(english, english_freq)
main(cyrillic, cyrillic_freq)
main(hiragana, hiragana_freq)
main(arabic, arabic_freq)

print("=====================================================\n")

print("Random values for sets of n frequencies")
print("---------------------------------------\n")

for x in range(1, 11):
    randomFreq(x * 10)
