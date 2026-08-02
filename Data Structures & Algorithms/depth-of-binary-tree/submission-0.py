# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        stack = [[root,1]]
        res = 0

        while stack:
            temp,depth = stack.pop()
            res = max(res, depth)
            if temp.right:
                stack.append([temp.right, depth+1])
            if temp.left:
                stack.append([temp.left, depth+1])
        return res


        