# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # if not root:
        #     return []

        # res =[]
        # que = deque([root])
        # while que:
        #     temp =[]
        #     for _ in range(len(que)):
        #         node = que.popleft()
        #         temp.append(node.val)
        #         if node.left:
        #             que.append(node.left)
        #         if node.right:
        #             que.append(node.right)
        #     res.append(temp)
        # return res

        res = []
        def dfs(root, depth):
            if not root:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        dfs(root, 0)
        return res
            


                

        


        