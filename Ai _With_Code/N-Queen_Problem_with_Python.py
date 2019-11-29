# N-Queen Problem: Solution in Python -Position Based & All Possible Solutions
""" N - Queens problem

*The n – queen problem is the generalized problem of 8-queens or 4 – queen’s problem. 
Here, the n – queens are placed on a n * n chess board, 
which means that the chessboard has n rows and n columns and
the n queens are placed on thus n * n chessboard such that no two queens are placed in the same row or in the same column or in same diagonal. 
So that, no two queens attack each other. 
"""

"""
*N-Queens Problem- A type of Constraint Satisfactory Problem in Artificial Intelligence
In this problem, we have an NxN square grid board and we have N queens which need to be placed on them. The queens should be placed on the board in such a way so that it satisfies the below-mentioned constraints:

No row should contain more than one queen placed in it
No column should contain more than one queen placed in it.
Not more than one queen should be placed in the single diagonal.
No row or column should be left without any queen placed in it.
On summing up all the constraints, we can conclude that each row and each column should contain exactly one queen in them, neither more nor less than that.

"""

"""
Algorithm

For all the solutions of the n - queen’s problem...

1. Algorithm N Queen (k, n)

2. // Using backtracking, this procedure prints all possible placements of

3. // n- queens on the n*n chess board so that they are non-attacking.

4. {

5. For I = 1 to n do

6. {

7. If Place (k, i) then

8. {

9. X[k] = I;

10. If (k = n) then write (x[1: n ]) ;

11.  Else N Queens (k+1, n);

12. }

13. }

14. }

"""

######################################################################################


#Simple 8-Queen Problem:  Solution in Python --Position based

BOARD_SIZE = 8

def under_attack(col, queens):

    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

def solve(n):

    solutions = [[]]

    for row in range(n):

        solutions = (solution+[i+1]

                       for solution in solutions # first for clause is evaluated immediately,

                                                 # so "solutions" is correctly captured

                       for i in range(BOARD_SIZE)

                       if not under_attack(i+1, solution))

    return solutions



answers = solve(BOARD_SIZE)

first_answer = next(answers)

print(list(enumerate(first_answer, start=1)))

#########################################################################################

# N-Queen Problem : All solutions in Python --ALL POSSIBLE SOLUTIONS

class QueenChessBoard:

    def __init__(self, size):

        # board has dimensions size x size

        self.size = size

        self.columns = []

 

    def place_in_next_row(self, column):

        self.columns.append(column)

 

    def remove_in_current_row(self):

        return self.columns.pop()

 

    def is_this_column_safe_in_next_row(self, column):

        # index of next row

        row = len(self.columns)

 

        # check column

        for queen_column in self.columns:

            if column == queen_column:

                return False

 

        # check diagonal

        for queen_row, queen_column in enumerate(self.columns):

            if queen_column - queen_row == column - row:

                return False

 

        # check other diagonal

        for queen_row, queen_column in enumerate(self.columns):

            if ((self.size - queen_column) - queen_row

                == (self.size - column) - row):

                return False

 

        return True

 

    def display(self):

        for row in range(self.size):

            for column in range(self.size):

                if column == self.columns[row]:

                    print('Q', end=' ')

                else:

                    print('.', end=' ')

            print()

 

 

def solve_queen(size):

    """Display a chessboard for each possible configuration of placing n queens

    on an n x n chessboard and print the number of such configurations."""

    board = QueenChessBoard(size)

    number_of_solutions = 0

 

    row = 0

    column = 0

    # iterate over rows of board

    while True:

        # place queen in next row

        while column < size:

            if board.is_this_column_safe_in_next_row(column):

                board.place_in_next_row(column)

                row += 1

                column = 0

                break

            else:

                column += 1

 

        # if could not find column to place in or if board is full

        if (column == size or row == size):

            # if board is full, we have a solution

            if row == size:

                board.display()

                print()

                number_of_solutions += 1

 

                board.remove_in_current_row()

                row -= 1

 

            # now backtrack

            try:

                prev_column = board.remove_in_current_row()

            except IndexError:

                # all queens removed

                # thus no more possible configurations

                break

            # try previous row again

            row -= 1

            # start checking at column = (1 + value of column in previous row)

            column = 1 + prev_column

 

    print('Number of solutions:', number_of_solutions)

 

n = int(input('What is the size of the chessboard? N='))

solve_queen(n)