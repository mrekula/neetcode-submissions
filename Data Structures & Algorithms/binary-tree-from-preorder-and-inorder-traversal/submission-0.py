# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        def dfs(preorder, inorder):
            if not preorder and not inorder:
                return None
            root = TreeNode(preorder[0])
            pivot = inorder.index(preorder[0])
            root.left = dfs(preorder[1:pivot+1], inorder[:pivot])
            root.right = dfs(preorder[pivot+1:], inorder[pivot+1:])
            return root
        return dfs(preorder,inorder )

        