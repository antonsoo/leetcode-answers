# 589. N-ary Tree Preorder Traversal - Easy - 2022Q3: Goog
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # recursive solution: O(N) time and space.
    def preorder2(self, root: 'Node') -> List[int]:
        output = []
        def helper(node):
            if not node:
                return 
            output.append(node.val)
            for child in node.children:
                helper(child)
        helper(root)
        return output
    

    
    # iterative/DFS solution: O(N) time and space
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root, ]
        output = []
        while stack:
            root = stack.pop()
            output.append(root.val) 
            stack.extend(root.children[::-1]) # extend adds the list/iterable element by element. 
        return output
        
            # Reason for reversal: "We know that stack is a First In Last Out data structure. Since we need to traverse the children Left -> Right, we can pop the left most child first only if we insert then right most child first into the stack.
#children = [1, 2, 3, 4] => stack = [4, 3, 2, 1]"



 # BFS/layerwise solution: O(N) time and space.... wrong thing to do for this question lol. It's asking us to do preorder traversal.
    def preorder2(self, root: 'Node') -> List[int]:
        if not root:
            return []
        queue = collections.deque([(root, root.val)])
        output = []    
        while queue:
            currnode, currval = queue.popleft()
            if currnode:
                output.append(currval)
                if currnode.children:
                    for childnode in currnode.children:
                        queue.append((childnode, childnode.val))
        return output
