# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # res=[]
        # def dfs(node, max_val):
        #     if not node:
        #         return 
        #     if node.val >= max_val:
        #         res.append(node.val)

        #     max_val = max(max_val, node.val)
        #     dfs(node.right, max_val)
        #     dfs(node.left, max_val)
        # dfs(root, float('-inf'))
        # print(res)
        # return len(res)

        count =0

        que = collections.deque([(root, float('-inf'))])

        while que:
            curr, max_val = que.popleft()
            if curr.val >= max_val:
                count += 1
            if curr.left:
                que.append((curr.left, max(max_val, curr.val)))
            if curr.right:
                que.append((curr.right, max(max_val, curr.val)))
        return count

            
        