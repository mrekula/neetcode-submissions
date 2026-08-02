# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        res=[]

        que= collections.deque([root])

        while que:
            temp=[]
            qlen = len(que)
            for _ in range(qlen):
                curr = que.popleft()
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                temp.append(curr.val)
            res.append(temp)
        return res
                
        


        