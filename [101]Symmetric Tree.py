# Given a binary tree, check whether it is a mirror of itself (ie, symmetric aro
# und its center). 
# 
#  For example, this binary tree [1,2,2,3,4,4,3] is symmetric: 
# 
#  
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  But the following [1,2,2,null,3,null,3] is not: 
# 
#  
#     1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  Follow up: Solve it both recursively and iteratively. 
#  Related Topics Tree Depth-first Search Breadth-first Search 
#  👍 5115 👎 123


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def convert_tree_to_symmetric(node):
            if node is None:
                return

            node.left, node.right = node.right, node.left
            convert_tree_to_symmetric(node.left)
            convert_tree_to_symmetric(node.right)
            return node

        def pre_travel_tree(node):
            if node is None:
                return None
            return [node.val, pre_travel_tree(node.left), pre_travel_tree(node.right)]

        return pre_travel_tree(root) == pre_travel_tree(convert_tree_to_symmetric(root))

# leetcode submit region end(Prohibit modification and deletion)
