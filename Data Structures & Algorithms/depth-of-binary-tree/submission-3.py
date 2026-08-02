# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # def dfs(root):

        #     if not root:
        #         return 0
            
        #     return 1+max(dfs(root.left), dfs(root.right))
        # return dfs(root)

        if not root:
            return 0
        stack =[[root,1]]
        res =1

        while stack:
            node, temp_len = stack.pop()
            res = max(res, temp_len)
            if node.left:
                stack.append([node.left,temp_len+1])
            if node.right:
                stack.append([node.right, temp_len+1])
        return res



        