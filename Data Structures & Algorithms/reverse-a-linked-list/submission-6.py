# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # current = head
        # prev= None

        # while current:
        #     temp = current.next 
        #     current.next = prev
        #     prev = current
        #     current = temp
        # return prev

        def dfs(head, prev):
            if not head:
                return prev
            temp = head.next
            head.next = prev
            return dfs(temp,head)
        return dfs(head, None)
        

        