class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        
        # If we find either p or q, return the node
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q found in different subtrees
        if left and right:
            return root
        
        # Otherwise return whichever is non-null
        return left if left else right
