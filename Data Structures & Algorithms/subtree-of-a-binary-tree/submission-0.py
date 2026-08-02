# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:



        def issame(root, subRoot):
            if not subRoot:
                return True
            if not root:
                return False
            if exact(root,subRoot):
                return True
            return (issame(root.left, subRoot) or issame(root.right, subRoot))
        def exact(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return (exact(root.left, subRoot.left) and exact(root.right, subRoot.right))
            return False
        return issame(root, subRoot)