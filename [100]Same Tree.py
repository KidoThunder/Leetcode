# Given two binary trees, write a function to check if they are the same or not.
#  
# 
#  Two binary trees are considered the same if they are structurally identical a
# nd the nodes have the same value. 
# 
#  Example 1: 
# 
#  
# Input:     1         1
#           / \       / \
#          2   3     2   3
# 
#         [1,2,3],   [1,2,3]
# 
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input:     1         1
#           /           \
#          2             2
# 
#         [1,2],     [1,null,2]
# 
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input:     1         1
#           / \       / \
#          2   1     1   2
# 
#         [1,2,1],   [1,1,2]
# 
# Output: false
#  
#  Related Topics Tree Depth-first Search 
#  👍 2682 👎 74


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_list = self.pre_travel(p)
        q_list = self.pre_travel(q)
        return q_list == p_list

    def pre_travel(self, node):
        if node is None:
            return None
        return [node.val, self.pre_travel(node.left), self.pre_travel(node.right)]

# leetcode submit region end(Prohibit modification and deletion)
