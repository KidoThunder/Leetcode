# Given a binary tree, flatten it to a linked list in-place. 
# 
#  For example, given the following tree: 
# 
#  
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
#  
# 
#  The flattened tree should look like: 
# 
#  
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#  
#  Related Topics Tree Depth-first Search 
#  👍 3623 👎 384


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        p = root

        while p.right is not None:
            p = p.right

        p.right = right

# leetcode submit region end(Prohibit modification and deletion)
