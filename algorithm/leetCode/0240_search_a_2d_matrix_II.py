"""
240. Search a 2D Matrix II
"""

class Solution:
    def searchMatrix(self, matrix, target):
        row, col = len(matrix)-1, 0

        while row >= 0 and col < len(matrix[0]):
            if target > matrix[row][col]:
                col += 1
            elif target < matrix[row][col]:
                row -= 1
            else:
                return True

        return False

