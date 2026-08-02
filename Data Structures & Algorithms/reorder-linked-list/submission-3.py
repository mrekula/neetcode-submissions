# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        out =[]
        current = head

        while current:
            out.append(current)
            current= current.next
        i, j = 0 , len(out)-1

        while i < j:
            out[i].next =out[j]
            i += 1
            if i==j:
                break
            out[j].next = out[i]
            j -= 1
        out[i].next = None

        
        