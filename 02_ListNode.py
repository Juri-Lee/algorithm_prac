class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList :
    def __init__(self):
        self.head = None

    def append(self,val):
        if not self.head:
            self.head = ListNode(val,None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val,None)


def mergeTwoLists(self,l1:ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l1.val > l2.val and l2):
        l1, l2 = l2, l1

    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)

    return l1

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

def resversLists(self, l1:ListNode) ->ListNode:
    def reverse(node : ListNode, list: ListNode) -> ListNode:
        if not node:
            return list


