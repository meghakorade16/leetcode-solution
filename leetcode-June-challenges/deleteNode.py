class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(self, node):
    if node.next is not None:
        node.val, node.next = node.next.val, node.next.next


if __name__ == '__main__':
    deleteNode()
