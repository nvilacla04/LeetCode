# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            res.append(node.val)
            visit(node.right)

        visit(root)
        return res