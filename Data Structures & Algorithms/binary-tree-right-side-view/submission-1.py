# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        que = collections.deque([(root,0)])
        level=0
        res=[]

        while que:
            n = len(que)
            for _ in range(n):
                curr, level = que.popleft()
                if curr.left:
                    que.append((curr.left, level+1))
                if curr.right:
                    que.append((curr.right, level+1))
            res.append(curr.val)
        return res


        