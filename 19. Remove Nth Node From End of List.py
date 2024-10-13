# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0, head)
        dummy = res

        for i in range(n):
            head = head.next

        while head:
            dummy = dummy.next # type: ignore
            head = head.next
        
        dummy.next = dummy.next.next  # type: ignore

        return res.next