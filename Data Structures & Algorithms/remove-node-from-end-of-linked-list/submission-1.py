# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # curr= head

        # node=[]
        # while curr:
        #     node.append(curr)
        #     curr = curr.next

        # target_node = len(node)-n
        # if node[target_node].next:
        #     node[target_node-1].next =node[target_node+1] 
        # else:
        #     node[target_node-1].next = None
        # return head

        # dummy = ListNode(0)
        # dummy.next = head
        # curr= dummy

        # for _ in range(n-1):
        #     curr = curr.next

        # curr.next= curr.next.next 
        # return dummy.next

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast= head

        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next






        



        