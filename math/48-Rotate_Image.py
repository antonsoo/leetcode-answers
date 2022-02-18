""" 48. Rotate Image - Medium - Amazon, Google, etc.
- problem: rotate a square matrix by 90 degrees clockwise (same as transposing and reversing)
"""
class Solution:
    # solution 1: rotate each corner of the matrix by 90 degrees clockwise. then move the corners inwards.
    # O(N) time (N is the total number of cells in the square matrix), O(1) space 
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) # n by n square matrix
        for i in range(n // 2 + n % 2):  # our last run will be over the middle point i and j
            for j in range(n // 2): 
                # maybe this can be done elegantly/Pythonically but lets just practice writing this
                # have to write n-1 because that's the actual last index 
                # set the bottomLeft temp value:
                bottomLeft = matrix[n - 1 - j][i] 
                # set the bottomLeft to the bottomRight val
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # set the bottomRight to the  topRight val
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # set the topRight to the topLeft val
                matrix[j][n - 1 - i] = matrix[i][j]
                # set the topLeft (originally the first index) to the bottomLeft val
                matrix[i][j] = bottomLeft
       
    
    
    
    # solution 2: transpose and reverse = 90 degree clockwise rotation
    # O(N) time (N is the total number of cells in the square matrix), O(1) space 
    def rotate2(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    # transposes by reflecting over the diagonal, starts outside and moves inside more and more
    def transpose(self, matrix): 
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
    # reflects over roughly the middle, starts outside (leftmost and rightmost columns), and goes inside more and more
    def reflect(self, matrix):  
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2): # roughly the middle
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
    
    
    def rotate3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # doesn't work because we're only allowed to modify in place
        #new_matrix = []
        #for row in zip(*matrix): # transposes the matrix
        #    new_matrix += row
        #matrix = list(zip(*matrix[::-1]))
        #return matrix
        
        
    
