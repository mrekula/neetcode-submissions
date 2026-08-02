# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # if not head:
        #     return 
        
        # curr = head
        # node=[]

        # while curr:
        #     node.append(curr)
        #     curr= curr.next
        # i, j = 0, len(node)-1

        # while i < j:
        #     node[i].next = node[j]
        #     i += 1
        #     if i ==j:
        #         break
        #     node[j].next = node[i]
        #     j -= 1
        # node[i].next = None

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next

        prev =slow.next= None

        while second:
            nxt = second.next
            second.next =prev
            prev= second
            second= nxt
        first, second = head, prev

        while second:
            temp1 = first.next
            temp2= second.next
            first.next = second
            second.next =temp1
            first, second = temp1, temp2


        
        