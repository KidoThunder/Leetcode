# Given the root of a binary tree, return all duplicate subtrees. 
# 
#  For each kind of duplicate subtrees, you only need to return the root node of
#  any one of them. 
# 
#  Two trees are duplicate if they have the same structure with the same node va
# lues. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,1,1]
# Output: [[1]]
#  
# 
#  Example 3: 
# 
#  
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the tree will be in the range [1, 10^4] 
#  -200 <= Node.val <= 200 
#  
#  Related Topics Tree 
#  👍 1675 👎 225


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        seen_subtree = defaultdict(int)
        res = list()
        self.range_each_subtree(root, res, seen_subtree)
        return res

    def range_each_subtree(self, root, res, seen_subtree):
        if root is None:
            return "#"

        left = self.range_each_subtree(root.left, res, seen_subtree)
        right = self.range_each_subtree(root.right, res, seen_subtree)
        subtree = str(left) + "," + str(right) + "," + str(root.val)

        seen_subtree[subtree] += 1
        if seen_subtree[subtree] == 2:
            res.append(root)
        return subtree

# leetcode submit region end(Prohibit modification and deletion)
