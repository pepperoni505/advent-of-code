import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    file_data = f.read().splitlines()

# Get order of numbers to draw
draw_numbers = list(map(int, file_data[0].split(",")))

# Get all boards
def getBoards():
    boards = [] # Array of boards. Each board is a list containing 5 lists, each representing each row in the bingo board

    current_board = []
    for i, line in enumerate(file_data[2:]):
        if line == "": # This represents a new board
            boards.append(current_board)
            current_board = []
            continue
        
        # Convert to list and remove blank spaces
        current_row = list(filter(None, line.split(" ")))
        # Convert to list of ints
        current_row = list(map(int, current_row))
        current_board.append(current_row)

        if i + 1 == len(file_data[2:]): # If we're at the end of the file, add the current board to boards
            boards.append(current_board)
    
    return boards

def getSumOfBoard(board):
    sum = 0
    for line in board:
        for item in line:
            if isinstance(item, int): # We need this check because we replace ints with X when they are drawn
                sum += item
    return sum

# Draw numbers
def drawNumbers(winningBoardNumber): # return winning board at index from winningBoardNumber. e.g. if winningBoardNumber is 3, return the 3rd winning board
    boards = getBoards()

    winningBoardsCount = 0
    winningBoards = [] # List of winning board indexes
    for number in draw_numbers:
        # Go through all boards and check if drawn number is present. If so, replace with an X
        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                for k, item in enumerate(line):
                    if item == number:
                        boards[i][j][k] = "X"
        
        # Check if board has all X in a row
        for i, board in enumerate(boards):
            # Horizontal check
            for line in board:
                if line.count("X") == len(line):
                    if i not in winningBoards: # Make sure board hasn't already won
                        # Bingo
                        if winningBoardsCount == winningBoardNumber:
                            sum_of_board = getSumOfBoard(board)
                            return sum_of_board * number
                        else:
                            winningBoardsCount += 1
                            winningBoards.append(i)

            # Vertical check
            for j in range(len(board[0])):
                column = []
                for line in board:
                    column.append(line[j])

                # Check if all values are X
                if column.count("X") == len(column):
                    if i not in winningBoards: # Make sure board hasn't already won
                        # Bingo
                        if winningBoardsCount == winningBoardNumber:
                            sum_of_board = getSumOfBoard(board)
                            return sum_of_board * number
                        else:
                            winningBoardsCount += 1
                            winningBoards.append(i)

print("Part 1: " + str(drawNumbers(0)))

print("Part 2: " + str(drawNumbers(len(getBoards()) - 1))) # Get the last winning board. I'm honestly not entirely sure why we have to subtract 1, but it works