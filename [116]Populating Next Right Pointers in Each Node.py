# You are given a perfect binary tree where all leaves are on the same level, an
# d every parent has two children. The binary tree has the following definition: 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#  
# 
#  Populate each next pointer to point to its next right node. If there is no ne
# xt right node, the next pointer should be set to NULL. 
# 
#  Initially, all next pointers are set to NULL. 
# 
#  
# 
#  Follow up: 
# 
#  
#  You may only use constant extra space. 
#  Recursive approach is fine, you may assume implicit stack space does not coun
# t as extra space for this problem. 
#  
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function sho
# uld populate each next pointer to point to its next right node, just like in Fig
# ure B. The serialized output is in level order as connected by the next pointers
# , with '#' signifying the end of each level.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the given tree is less than 4096. 
#  -1000 <= node.val <= 1000 
#  Related Topics Tree Depth-first Search Breadth-first Search 
#  👍 2804 👎 154


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
"""


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None or root.left is None:
            return root
        self.connect_tow_node(root.left, root.right)
        return root

    def connect_tow_node(self, node_1, node_2):
        if node_1 is None or node_2 is None:
            return

        node_1.next = node_2
        self.connect_tow_node(node_1.left, node_1.right)
        self.connect_tow_node(node_2.left, node_2.right)
        self.connect_tow_node(node_1.right, node_2.left)

    # leetcode submit region end(Prohibit modification and deletion)
