# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hashet = set()

        curr = head

        while curr:
            if not curr.next:
                return False
            elif curr in hashet:
                return True
            else:
                hashet.add(curr)
            curr = curr.next
        return False
        

        