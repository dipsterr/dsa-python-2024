from typing import Optional


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = Node(0)
        temp = dummy
        carry = 0
        
        while (l1!=None or l2!=None) or carry:
            sum = 0
            if l1!=None:
                sum += l1.data
                l1 = l1.next
            if l2!=None:
                sum += l2.data
                l2 = l2.next
            sum += carry
            carry = sum//10
            node = Node(sum%10)
            temp.next = node
            temp = temp.next
        return dummy.next

        # pass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# Utility function to print the list


def printList(n):
    while n:
        print(n.data, end = ' ')
        n = n.next
    print()


# Driver Code
if __name__ == "__main__":

    arr1 = [7, 5, 9, 4, 6]
    LL1 = LinkedList()
    for i in arr1:
        LL1.insert(i)
    print("First list is", end = " ")
    printList(LL1.head)

    arr2 = [8, 4]
    LL2 = LinkedList()
    for i in arr2:
        LL2.insert(i)
    print("Second list is", end = " ")
    printList(LL2.head)

    # Function Call
    res = Solution().addTwoNumbers(LL1.head, LL2.head)
    print("Resultant list is", end = " ")
    print (res)
    printList(res)

# This code Contributed by Vaidehi Agarwal
