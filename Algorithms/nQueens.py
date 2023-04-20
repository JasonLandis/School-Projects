import timeit
import random
import copy
import csv

solutions = []  # Keeps track of number of solutions
time = []   # Keeps track of elapsed time after each solution is found
boards = [] # Keeps track of all the solution boards
nodes = [] # Keeps track of the actual nodes generated
inputs = [] # Stores input list

# Asks user for value of n with error handling
def createBoard():
    # Reads example input from file
    count = 0
    with open('input.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inputs.append(''.join(row))

    while True: 
        n = inputs[count]
        count += 1

        # Enable line below to specify your own values of n        
        # n = input("(type n to quit) Enter the value of n: ")

        if n == 'n':
            exit()
        try:
            n = int(n)
        except ValueError:
            print("Enter an integer")
            createBoard()

        if n == 2 or n == 3:
            print("There is no solution for n =", n)
            createBoard()
        if n < 1 or n > 10:
            print("Input a value between 1 and 10")
            createBoard()
        else:
            # Creates n x n matrix of '▪ '
            board = [['▪ ' for x in range(n)] for y in range(n)]
            print()
            start = timeit.default_timer()
            print("Running program for n =", n)
            print()
            main(board, 0, start)

            # Once the main program is finished, it gets a random solution board
            # and sends it to the getEstimateValues() function
            rand_board =  boards[random.randrange(0, len(boards))]
            getEstimateValues(rand_board, n - 1, n - 1)

            # Reads the timing data to a csv file to easily export
            with open('times.csv', 'w', newline='') as file:
                write = csv.writer(file)
                for w in range(len(time)):
                    write.writerow([time[w]])
                file.close()

            # Clears all the lists in case you want to enter another value for n
            solutions.clear()
            time.clear()
            boards.clear()
            nodes.clear()
            estimate.clear()
            sum_estimate.clear()
            sum_estimate.append(1)


# Determines if a spot is safe to place a queen
def isSafe(board, row, col):
    # Checks if two queens share the same column
    for x in range(row):
        if board[x][col] == '♛ ':            
            return False

    # Checks if two queens share the same negative diagonal
    (x, y) = (row, col)
    while x >= 0 and y >= 0:
        if board[x][y] == '♛ ':
            return False
        x -= 1
        y -= 1

    # Checks if two queens share the same positive diagonal
    (x, y) = (row, col)
    while x >= 0 and y < len(board):
        if board[x][y] == '♛ ':
            return False                       
        x -= 1
        y += 1

    # Returns true if queen can safely be placed              
    return True

    
# Prints solution in matrix format
def printSolution(board):       
    solutions.append(1)
    print("Solution Number", sum(solutions))
    for row in board:
        print(" ".join(row))
    print("Elapsed Time:", time[sum(solutions) - 1], "milliseconds\n")


# Main function that recurs for each row
def main(board, row, start):
    if row == len(board):
        time.append((timeit.default_timer() - start) * 1000)
        solution_board = copy.deepcopy(board)
        boards.append(solution_board)        
        printSolution(board)

    # Adds node to the list
    nodes.append(1)
    
    # Checks each square and runs isSafe() function
    for x in range(len(board)):
        if isSafe(board, row, x):
            # Backtracking algorithm            
            board[row][x] = '♛ '
            main(board, row + 1, start)            
            board[row][x] = '▪ '

# ---------------------------------------------------------------------------------------------------------
# Estimate portion of the program
# ---------------------------------------------------------------------------------------------------------

estimate = []  # Stores values to be used in the Estimate() function
sum_estimate = [1]  # Stores values of numbers found in the recursie Estimate() function to be added

# This function uses a solution board and follows row by row to detect if a queen can be placed
# It returns the values to be sent to the Estimate() function
def getEstimateValues(board, row, col): 
    n = row + 1    
    count = 1
    row_count = 1

    estimate.append(n)
    sum_estimate.append(n)

    print("----------------------------------------------------\n")
    print("Estimate Algorithm")   
    print("Randomly chosen estimate board:")
    for x in board:
        print(" ".join(x))
    print("Starting possible locations:", n)     

    # Creates an empty board
    new = [['▪ ' for x in range(n)] for y in range(n)]        
    new[0] = board[0]
    
    for x in range(row):                
        for y in range(col + 1):            
            if new[x][y] == '♛ ': 
                # Marks 'x' on all column spaces under a queen               
                while x + count != n:                                        
                    new[x + count][y] = 'x '                    
                    count += 1
                count = 1
                # Marks 'x' on all spaces under a queen on the negative diagonal
                while x + count != n and y + count != n:
                    new[x + count][y + count] = 'x '                    
                    count += 1
                count = 1
                # Marks 'x' on all spaces under a queen on the positive diagonal
                while x + count != n and y - count != -1:
                    new[x + count][y - count] = 'x '                    
                    count += 1

        # Checks which spaces a queen can be placed and stores data
        count = 0
        for x in new[row_count]:
            if x != 'x ':
                count += 1
        estimate.append(count)

        # Prints each iteration of above function
        print()
        print("Iteration:", row_count)
        for x in new:
            print(" ".join(x))
        print("Possible locations:", count)       

        # Replaces each row of 'new' empty board with row of original board
        new[row_count] = board[row_count]
        row_count += 1
        count = 1

    Estimate(n, count)

# Estimate() function uses recursion to send values to sum_list
def Estimate(num, count):
    if count != len(estimate):
        num = num * estimate[count]
        sum_estimate.append(num)
        Estimate(num, count + 1)
    else:
        print()
        print("Estimated nodes generated:", estimate, "=", sum(sum_estimate))
        print("Actual nodes generated:", sum(nodes))
        print()
        print("====================================================")
        return

# Function call to create board
createBoard()
