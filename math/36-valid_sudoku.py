""" 36. Valid Sudoku. Medium+
- problem: validate sudoku board
each row and each column will have unique numbers 1-9 (or nothing) to that row or column.
each 3x3 sub-boxes will also contain unique 1-9 numbers.
- other brilliant (and difficult-to-understand) solutions : https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
"""
from collections import Counter
class Solution:
    
    # goes through the rows, columns, and boxes at the same time
    def isValidSudoku(self, board: List[List[str]]) -> bool:   # https://leetcode.com/problems/valid-sudoku/discuss/511365/Simple-Intuitive-Python-Approach
        # makes 9 sets for all 9 rows, all 9 colums, and all 9 boxes
        rows = [set() for i in range(9)] 
        cols = [set() for i in range(9)]
        mMat = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    k = (i // 3 ) * 3 + j // 3 # i,j=0,1,2 will be box 0,   i=0,1,2;j=3,4,5 will be box 1,    etc.
                
                    if cur not in rows[i]: rows[i].add(cur)
                    else: return False
                    
                    if cur not in cols[j]: cols[j].add(cur)
                    else: return False
                
                    if cur not in mMat[k]: mMat[k].add(cur) # boxes (from top left to righ) are: 0, 3, 6,;   1, 4, 7,;     2, 5, 8
                    else: return False
        return True
    
    
    
    
    
    
    
    
    # O(N^2) time, O(N^2) time. technically it's ~O(1) because we know the exact size of N, which is 9
    def isValidSudoku2(self, board):
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board): # zip(*board) turns every row into a column and vice versa
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True
    
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
    
    
    
    
    
    
    
    
    
    def isValidSudoku4(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            col_counts = {"." : -9} 
            col_counts.update(Counter(board[row])) # merge with the set of counters
            for key, item in col_counts.items(): # don't start at "."
                if item > 1:
                    return False
        for col in range(len(board)):
            row_counts = {"." : -9}
            row_counts.update(Counter([col]))
            for key, item in row_counts.items(): # don't start at "."
                if item > 1:
                    return False
        return True
    
    
    
    
    
    
    
    def isValidSudoku5(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            col_nums = []
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in col_nums:
                    print("bleh", col_nums)
                    return False
                else:
                    print(col_nums)
                    col_nums += board[row][col]
        for col in range(len(board)):
            row_nums = []
            for row in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in row_nums:
                    print("blassah", row_nums)
                    return False
                else:
                    row_nums += board[col][row]
        return True
