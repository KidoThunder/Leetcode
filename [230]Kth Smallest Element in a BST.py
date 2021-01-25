# Given a binary search tree, write a function kthSmallest to find the kth small
# est element in it. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1 
# 
#  Example 2: 
# 
#  
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
#  
# 
#  Follow up: 
# What if the BST is modified (insert/delete operations) often and you need to f
# ind the kth smallest frequently? How would you optimize the kthSmallest routine?
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of elements of the BST is between 1 to 10^4. 
#  You may assume k is always valid, 1 ≤ k ≤ BST's total elements. 
#  
#  Related Topics Binary Search Tree 
#  👍 3439 👎 79


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    rank = 0
    res = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.traverse(root, k)
        return self.res

    def traverse(self, root, k):
        if root is None:
            return

        self.traverse(root.left, k)

        self.rank += 1
        if k == self.rank:
            self.res = root.val
            return

        self.traverse(root.right, k)


















        
# leetcode submit region end(Prohibit modification and deletion)
