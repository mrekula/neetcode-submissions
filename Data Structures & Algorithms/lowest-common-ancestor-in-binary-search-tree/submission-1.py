# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # def dfs(root, p, q):

        #     if not p or not q or not root:
        #         return None

        #     if max(p.val,q.val) < root.val:
        #         return dfs(root.left, p, q)
        #     elif min(p.val,q.val) > root.val:
        #         return dfs(root.right, p, q)
        #     else:
        #         return root
        # return dfs(root, p, q)


        curr = root

        while curr:
            if max(p.val,q.val) < curr.val:
                curr = curr.left
            elif min(p.val, q.val) > curr.val:
                curr = curr.right
            else:
                return curr

        
        