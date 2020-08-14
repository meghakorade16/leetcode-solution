from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode):
        if not root:
            return []
        queue = deque([(root, 0)])
        lst, result = [], []
        while queue:
            node, h = queue.popleft()
            if node.left:
                queue.append((node.left, h - 1))
            if node.right:
                queue.append((node.right, h + 1))
            lst.append([h, node.val])
        k = float('-inf')
        i = -1
        for c, val in sorted(lst, key=lambda x: x[0]):
            if k == c:
                result[i].append(val)
            else:
                result[i].append([val])
                k = c
                i += 1
        return result
