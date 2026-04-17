# LC 867. Transpose Matrix
# Solution: https://leetcode.com/problems/transpose-matrix/solutions/6097971/video-give-me-5-minutes-2-solutions-how-ihrf8/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []

        for c in range(len(matrix[0])):
            temp = []

            for r in range(len(matrix)):
                temp.append(matrix[r][c])

            res.append(temp)

        return res
