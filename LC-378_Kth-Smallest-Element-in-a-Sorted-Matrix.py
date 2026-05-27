# Problem: 378. Kth Smallest Element in a Sorted Matrix
# Solution: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solutions/8279472/binary-search-solution-python3-clean-cod-xmdo/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def countLessEqual(x):
            count = 0
            j = n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > x:
                    j -= 1
                count += (j + 1)
            return count

        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
