# Problem link https://leetcode.com/problems/combination-sum/
# 39. Combination Sum
# Solution link: https://leetcode.com/problems/combination-sum/solutions/6146998/simple-solution
# Solution is from the user named niits
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            
        res = []

        def make_combination(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            
            if total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()
            make_combination(idx+1, comb, total)

            return res

        return make_combination(0, [], 0)
