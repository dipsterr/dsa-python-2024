class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def segregateEvenOdd(head):
    oddNode = node(-1)
    evenNode = node(-1)
    even_curr = evenNode #
    odd_curr = oddNode
    curr = head
    
    while curr:
        if curr.data % 2 == 0:
            even_curr.next = curr
            even_curr = even_curr.next

        else:
            odd_curr.next = curr
            odd_curr = odd_curr.next

        curr = curr.next
    
    # Terminate both lists
    even_curr.next = None
    odd_curr.next = None
    
    even_curr.next = oddNode.next
    return evenNode.next