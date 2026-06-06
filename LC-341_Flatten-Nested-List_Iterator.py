# Problem: 341. Flatten Nested List Iterator
# Solution: https://leetcode.com/problems/flatten-nested-list-iterator/solutions/8308407/linus-solutions-by-linuscodes56-z0ft/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, l: [NestedInteger]):
        self.l: list[int] = self.flatter_helper(l)
        self.i: int = 0
    
    def flatter_helper(self, l: [NestedInteger]) -> None:
        ans = []
        for i in range(0, len(l)):
            if l[i].isInteger():
                ans.append(l[i].getInteger())
            else:
                ans.extend(self.flatter_helper(l[i].getList()))

        return ans
    
    def next(self) -> int:
        curr_idx: int = self.i
        self.i += 1
        return self.l[curr_idx]

    def hasNext(self) -> bool:
        if self.i < len(self.l):
            return True
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
