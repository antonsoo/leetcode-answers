    def goodNodes(self, root: TreeNode) -> int:
        # counts the number of non-contiguous nodes in a path to a node, assuming no node previously seen in the path is bigger than that current node
        # O(n) worst time where n = num of nodes, O(n) worst space (because of the recursive callstack), where n=Heigh
        
        def dfs(node, cmax): # cmax is current max value of a node (seen so far)
            nonlocal ngood
            if cmax <= node.val:
                ngood += 1
                cmax = node.val
            if node.left: # if the left child of the node is not empty 
                dfs(node.left, cmax)
            if node.right:
                dfs(node.right, cmax)
            
            
        ngood = 0 # number of good nodes
        dfs(root, -math.inf)
        return ngood
