# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # out =[]
        # current = head

        # while current:
        #     out.append(current)
        #     current= current.next
        # i, j = 0 , len(out)-1

        # while i < j:
        #     out[i].next =out[j]
        #     i += 1
        #     if i==j:
        #         break
        #     out[j].next = out[i]
        #     j -= 1
        # out[i].next = None
    
        # 1. Midpoint
        if not head:
            return None
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2. reverse

        second = slow.next
        prev = None
        slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

 

        # 2. Merge
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2





        
        