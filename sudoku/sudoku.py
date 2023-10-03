sudoku = [[2, 0, 9, 0, 6, 0, 0, 0, 4],
          [0, 4, 0, 0, 1, 8, 3, 0, 9],
          [0, 1, 0, 9, 4, 0, 0, 7, 8],
          [9, 2, 0, 6, 0, 4, 1, 0, 0],
          [7, 0, 0, 0, 8, 0, 4, 9, 0],
          [0, 0, 0, 2, 0, 9, 8, 0, 3],
          [0, 0, 6, 4, 0, 0, 0, 3, 0],
          [5, 0, 4, 0, 9, 6, 0, 0, 0],
          [0, 3, 0, 0, 0, 0, 9, 4, 6]]

def box(row, column):
    box = []
    small_row, small_column = (row // 3) * 3, (column // 3) * 3 #Start row/column must be 0, 3, or 6, so always starts in top-left of box
    for i in range(small_row, small_row + 3): #Range constrains search to a 3x3 area
        for j in range(small_column, small_column + 3):
            box.append(sudoku[i][j])
    return box

def valid(row, column, number):
    for i in range(9):
        if number == sudoku[row][i] or number == sudoku[i][column] or number in box(row, column): #Searches the row, column, and box the number is in for duplicates
            return False
    return True

def solve(sudoku):
    for row in range(9):
        for column in range(9):#Cycles through each number

            if sudoku[row][column] == 0: #Checks for an empty space

                for number in range(1, 10):
                    print(f"Trying {number} in row {row}, column {column}.")
                    if valid(row, column, number): #If the number fits in this space:
                        sudoku[row][column] = number #Lock it into place
                        if solve(sudoku): #Starts a new function with the new number in place. If returned false, it will revert back to the previous position and continue through the number cycle.
                            return True
                        sudoku[row][column] = 0 #Resets the number before cycling through the next number in the range.

                return False #This works recursively and is meant for the "solve(sudoku)" inside this for loop. See above comment next to "if solve(sudoku)"
            
    return True #If we have reached this point it means that the sudoku is solved.

if __name__ == "__main__":
    if solve(sudoku):
        for row in range(9):
            print(sudoku[row])
        print("Your sudoku is solved!")
    else:
        print("Your sudoku cannot be solved. Check for any misplaced numbers.")
                        