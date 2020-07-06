class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(self, root: TreeNode):
    result = []
    index = 0
    if not root:
        return reversed(result)
    result.insert(index, [root.val])
    index += 1
    if root.left:
        root = root.left
    if root.right:
        root = root.right


