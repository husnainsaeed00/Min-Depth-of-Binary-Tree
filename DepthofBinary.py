class Solution(object):
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def minDepth(self, root):
        if not root:
            return 0

        # Check if the root is a leaf node
        if not root.left and not root.right:
            return 1

        # Calculate the minimum depth of the left and right subtrees
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # If either subtree is empty, return the depth of the non-empty subtree
        if not root.left:
            return right_depth + 1
        if not root.right:
            return left_depth + 1

        # Return the minimum depth of the tree
        return min(left_depth, right_depth) + 1
